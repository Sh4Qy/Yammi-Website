from flask import Flask
from db import db
from auth import login_manager,item_amount
from models.cart import Cart
from models.category import Category
from models.delivery import Delivery
from models.dish import Dish
from models.items import Items
from models.user import User
from routes.users import user_bp
from routes.dishes import dish_bp
from routes.orders import order_bp
from routes.categories import category_bp
from config import DBUSER,DBPASS,DBHOST

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mask84nt9auh3s8anj4'
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{DBUSER}:{DBPASS}@{DBHOST}/postgres'
db.init_app(app)
login_manager.init_app(app)


with app.app_context():
    db.create_all()


app.register_blueprint(user_bp)
app.register_blueprint(dish_bp,url_prefix='/dish')
app.register_blueprint(order_bp,url_prefix='/order')
app.register_blueprint(category_bp,url_prefix='/category')
app.jinja_env.globals.update(len=len)
app.jinja_env.globals.update(item_amount=item_amount)

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')