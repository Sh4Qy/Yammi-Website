from flask import Blueprint
from controllers.users import register,sign_in,edit_profile,log_out,main,add_admin

user_bp = Blueprint('user',__name__)

user_bp.add_url_rule('/', view_func=main)

user_bp.add_url_rule('/register',view_func=register,methods=['GET','POST'])

user_bp.add_url_rule('/sign-in',view_func=sign_in,methods=['GET','POST'])

user_bp.add_url_rule('/add-user',view_func=add_admin,methods=['GET','POST'])

user_bp.add_url_rule('/log-out',view_func=log_out)
 
user_bp.add_url_rule('/edit_profile',view_func=edit_profile,methods=['GET','POST'])