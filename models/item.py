from db import db 

#creating a function for internal representation of item 
class ItemModel(db.Model):
    # db.model is to tell sqlalchemy that these are things used to create an item 
    # In other words, it is used to create mapping b/w objects and database

    __tablename__= 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float(precision=2))
    # telling sqlalchemy that this Item model has 3cloumns

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    # store_id = db.Column(db.Integer, db.Foreignkey('stores.id')
    # store = db.relationship('StoreModel')
     # telling item that it has a relationship StoreModel in terms of id

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id


# creating func for json representation of item
    def json(self):
        return {'name':self.name, 'item':self.price}


# transfering all class method from resources.item file to models.item file
    @classmethod
    def find_by_name(cls, name):
       return cls.query.filter_by(name=name).first()
        #same as SELECT *  FROM items WHERE name=name(parameter of this func) LIMIT 1 

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()      
