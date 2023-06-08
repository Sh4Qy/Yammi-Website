from db import db
from sqlalchemy.ext.associationproxy import association_proxy

class Dish(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    price = db.Column(db.Integer,nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(500),nullable=False)
    is_gluten_free = db.Column(db.Boolean,nullable=False)
    is_vegeterian = db.Column(db.Boolean,nullable=False)
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    cart_association = db.relationship('Items', back_populates='dish')
    carts = association_proxy('cart_association', 'cart')