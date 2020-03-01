from flask import Flask,jsonify
from flask_restful import  Api
from flask_jwt import JWT
import datetime
from security import authenticate, identity as identity_function
from user import UserRegister
from item import Item,ItemList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
app.secret_key = 'jefefewg4erererer3'
app.config['JWT_AUTH_URL_RUL']='/login'
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=60*60/2)#30 min
# app.config['JWT_AUTH_USERNAME_KEY']='email'
api = Api(app)




jwt = JWT(app, authenticate, identity_function)#/login
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister,'/register')

if __name__ == '__main__':
    app.run(port =5000,debug=True)  # important to mention debug=True
