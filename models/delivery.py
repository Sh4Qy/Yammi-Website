from db import db

class Delivery(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    is_delivered = db.Column(db.Boolean,default=False)
    address = db.Column(db.String(200))
    comment = db.Column(db.Text)
    created = db.Column(db.DateTime)
    cart = db.relationship('Cart',backref='delivery',uselist=False)