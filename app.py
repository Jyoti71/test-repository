from flask import Flask
from flask_restful import  Api
# Request Parsing(REQPARSE)designed to provide simple and uniform access 
# to any variable on the flask.request object in Flask.
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from db import db 
from resources.store import Store, StoreList


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# turns off flask sqlalchemy modification tracker
app.secret_key= 'sneha'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)
#create new endpoint /auth
#This object is used to hold the JWT settings and callback functions. 
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
#  above line is equal to http://127.0.0.1:5000/item/chair same as @app.route
api.add_resource(StoreList, '/stores')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__": 
    db.init_app(app) 
    app.run(debug=True)
                