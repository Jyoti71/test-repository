from db import db 

class StoreModel(db.Model):
    # db.model is to tell sqlalchemy that these are things used to create an store
    # In other words, it is used to create mapping b/w objects and database

    __tablename__= 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    # telling sqlalchemy that this Item model has columns

    items = db.relationship('ItemModel', lazy = 'dynamic')
    # telling store that it has a relationsship ItemModel in terms of id

    def __init__(self, name):
        self.name = name
      
# creating func for json representation
    def json(self):
        return {'name':self.name, 'items': [item.json for item in self.items.all()]}

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
