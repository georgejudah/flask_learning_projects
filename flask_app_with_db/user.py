from datetime import datetime, timedelta
from html import parser
import sqlite3
from flask_restful import Resource, reqparse
from hmac import compare_digest
import jwt
import app


class User():
    TABLE_NAME = 'users'

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


class UserRegister(Resource):
    TABLE_NAME = 'users'

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO {table} VALUES (NULL, ?, ?)".format(table=self.TABLE_NAME)
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201
    
class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                    type=str,
                    required=True,
                    help="This field cannot be left blank!"
                    )
    parser.add_argument('password',
                    type=str,
                    required=True,
                    help="This field cannot be left blank!"
                    )
    def post(self):
        data = UserLogin.parser.parse_args()    
        user = User.find_by_username(data['username']) 
        if user and compare_digest(user.password, data['password']):
            token = jwt.encode({
            'username': data['username'],
            'exp' : datetime.utcnow() + timedelta(minutes = 20)
            }, "bubloo")

            #have enter the encoding private key here just for learning, should never be stored like this
            return ({'token' : token.decode('UTF-8')}), 201
        elif user:
            return{"message": "Invalid Credentials"}, 401
        else:
            return {"message": "Username or password incorrect"}, 401

