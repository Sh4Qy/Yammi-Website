from flask import Blueprint
from controllers.orders import (order_management,change_delivery_status,see_comment,see_comment_summary,order,show_cart
                                ,summary,delete_item,orders_history,add_to_cart)

order_bp = Blueprint('order',__name__)

order_bp.add_url_rule('/management',view_func=order_management)

order_bp.add_url_rule('/comment/<int:id>',view_func=see_comment)

order_bp.add_url_rule('/change_delivery_status/<int:id>',view_func=change_delivery_status,methods=['POST'])

order_bp.add_url_rule('/',view_func=order,methods=['GET','POST'])

order_bp.add_url_rule('/show_cart',view_func=show_cart)

order_bp.add_url_rule('/add_to_cart/<int:id>',view_func=add_to_cart,methods=['POST'])

order_bp.add_url_rule('/summary/<int:id>',view_func=summary)

order_bp.add_url_rule('/comment_summary/<int:id>',view_func=see_comment_summary)

order_bp.add_url_rule('/delete_item/<int:id>',view_func=delete_item,methods=['GET','POST'])

order_bp.add_url_rule('/history',view_func=orders_history)
