from flask import Blueprint
from controllers.dishes import show_dishes,add_dish,dish_management,edit_dish,delete_dish

dish_bp = Blueprint('dish',__name__)

dish_bp.add_url_rule('/show_dishes/<int:id>',view_func=show_dishes)

dish_bp.add_url_rule('/add',view_func=add_dish,methods=['GET','POST'])

dish_bp.add_url_rule('/management',view_func=dish_management)

dish_bp.add_url_rule('/edit/<int:id>',view_func=edit_dish,methods=['GET','POST'])

dish_bp.add_url_rule('/delete/<int:id>',view_func=delete_dish,methods=['GET','POST'])