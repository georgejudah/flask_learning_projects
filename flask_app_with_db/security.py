from functools import wraps
from flask import jsonify, request
from werkzeug.security import safe_str_cmp
from user import User
import jwt
from user import User

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password == password) :
        return username

def identity(payload):
    user_id = payload['identity']
    return User.find_by_id(user_id)

def token_required(f):
    def wrapper(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
            # print("received it")
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            #NEVER STORE YOUR KEYS LIKE THIS, THIS IS JUST FOR TESTING
            data = jwt.decode(token, 'bubloo')
            # print(data['username'])
            if User.find_by_username(data['username']):
                # print("logged in")
                return f(*args, **kwargs)
            else:
                return jsonify({'message' : 'Token is invalid'})
                
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # return f(*args, **kwargs)
        # # returns the current logged in users contex to the routes
        # return  f(current_user, *args, **kwargs)
  
    return wrapper
