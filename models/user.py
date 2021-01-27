import sqlite3
from db import db

class UserModel(db.Model):
    # db.model is used to create mapping b/w objects and database

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    # telling sqlalchemy that this  user model has 3cloumns


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()  
     
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()   
         #same as SELECT *  FROM items WHERE username=username(parameter of this func)LIMIT 1

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()
         #same as SELECT *  FROM items WHERE username=username(parameter of this func)LIMIT 1

  