from flask import Blueprint
from controllers.categories import add_category,category_management,delete_category,edit_category,menu

category_bp = Blueprint('category',__name__)

category_bp.add_url_rule('/menu',view_func=menu)

category_bp.add_url_rule('/management',view_func=category_management)

category_bp.add_url_rule('/add',view_func=add_category,methods=['GET','POST'])

category_bp.add_url_rule('/edit/<int:id>',view_func=edit_category,methods=['GET','POST'])

category_bp.add_url_rule('/delete/<int:id>',view_func=delete_category,methods=['GET','POST'])