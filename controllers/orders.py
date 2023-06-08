from flask import render_template,request,redirect,url_for,flash
from db import db
from flask_login import login_required,current_user
from models.dish import Dish
from models.form import Form
from models.category import Category
from models.delivery import Delivery
from models.cart import Cart
from models.items import Items
from models.user import User
from datetime import datetime as dt
from utils import is_staff

@login_required
def order_management():
    deliveries = Delivery.query.all()
    return is_staff('orders/order_management.html',delivery=deliveries)

@login_required
def see_comment(id):
    delivery = Delivery.query.get(id)
    return is_staff('orders/see_comment.html',delivery=delivery)

@login_required
def change_delivery_status(id):
    if request.method == 'POST':
        delivery = Delivery.query.get(id)
        delivery.is_delivered = True
        db.session.commit()
        return redirect(url_for('order.order_management'))
@login_required
def order():
    form = Form()
    cart = current_user.carts[-1]
    items = cart.dish_association
    cost = 0
    for item in items:
        cost += (item.amount * item.dish.price)
    if request.method == 'POST':
        new_delivery = Delivery(
            address = form.address.data,
            comment = form.comment.data,
            created = dt.now()
        )
        db.session.add(new_delivery)
        db.session.commit()
        cart.delivery_id = new_delivery.id
        new_cart = Cart(user_id = current_user.id)
        db.session.add(new_cart)
        db.session.commit()
        return redirect(url_for('order.summary',id=new_delivery.id))
    return render_template('orders/order.html',items=items,cost=cost,form=form,cart=cart)

@login_required
def show_cart():
    cart = current_user.carts[-1]
    items = cart.dish_association
    total_cost = 0
    for item in items:
        total_cost += (item.dish.price * item.amount)
    cart.total_cost = total_cost
    db.session.commit()
    return render_template('orders/show_cart.html',items=items,total_cost=total_cost)

@login_required
def add_to_cart(id):
    form = Form()
    dish = Dish.query.get(id)
    category = Category.query.get(dish.category.id)
    if request.method == 'POST':
        cart = current_user.carts[-1]
        if dish in cart.dishes:
            for item in cart.dish_association:
                    if item.dish == dish:
                        item.amount += int(form.amount.data)
                        db.session.commit()
                        flash(f'{item.dish.name} added to the cart','add')
                        return redirect(url_for('dish.show_dishes',id=category.id))
        else:
            add_dish_to_cart = Items(
                dish = dish,
                cart = cart,
                amount = form.amount.data
            )
            db.session.add(add_dish_to_cart)
            db.session.commit()
            flash(f'{dish.name} added to the cart','add')
            return redirect(url_for('dish.show_dishes',id=category.id))

@login_required
def delete_item(id):
    item = Items.query.get(id)
    if request.method == 'POST':
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('order.show_cart'))
    return render_template('orders/delete_item.html',item=item)

@login_required
def orders_history():
    total_cost = []
    cost = 0
    deliveries = [cart.delivery for cart in current_user.carts if cart.delivery != None]
    for delivery in deliveries:
        for item in delivery.cart.dish_association:
            cost += (item.amount * item.dish.price)
        total_cost.append(cost)
    return render_template('orders/orders_history.html',deliveries=deliveries,total_cost=total_cost)

@login_required
def summary(id):
    delivery = Delivery.query.get(id)
    return render_template('orders/summary.html',delivery=delivery)

@login_required
def see_comment_summary(id):
    delivery = Delivery.query.get(id)
    return render_template('orders/see_comment.html',delivery=delivery)