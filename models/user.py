from db import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(10),nullable=False,unique=True)
    password = db.Column(db.String(10),nullable=False)
    first_name = db.Column(db.String(20),nullable=False)
    last_name = db.Column(db.String(20),nullable=False)
    is_staff = db.Column(db.Boolean,nullable=False,default=False)
    email = db.Column(db.String(30))
    carts = db.relationship('Cart',backref='user')