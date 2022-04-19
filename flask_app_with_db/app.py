# from datetime import timedelta
from flask import Flask
from flask_restful import Api
# from flask_jwt import JWT

from item import Item, ItemList
from security import authenticate, identity
from user import UserRegister, UserLogin

app = Flask(__name__)
# app.config['PROPOGATE EXCEPTIONS'] = True
# app.secret_key = 'jose'

api = Api(app)

# jwt = JWT(app, authenticate, identity) #auth
# app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)






    

# http://127.0.0.1:5000/item/chair
api.add_resource(Item, '/item/<string:name>')

api.add_resource(ItemList, '/items')

api.add_resource(UserRegister, '/register')

api.add_resource(UserLogin, '/login')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

