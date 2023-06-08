from flask_login import current_user
from flask import url_for,redirect,render_template


def is_staff(html,category=None,dish=None,delivery=None,form=None,users=None):   
    if not current_user.is_staff:
        return redirect(url_for('dish.menu'))
    return render_template(html, category = category, dish = dish, delivery = delivery, form = form, users = users)