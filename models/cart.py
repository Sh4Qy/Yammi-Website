from db import db
from sqlalchemy.ext.associationproxy import association_proxy

class Cart(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    total_cost = db.Column(db.Integer,default=0)
    delivery_id = db.Column(db.Integer,db.ForeignKey('delivery.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    dish_association = db.relationship('Items', back_populates='cart')
    dishes = association_proxy('dish_association', 'dish')