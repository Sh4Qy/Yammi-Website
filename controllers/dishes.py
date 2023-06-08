from flask import render_template,request,redirect,url_for
from flask_login import login_required
from db import db
from models.category import Category
from models.dish import Dish
from models.form import Form
from utils import is_staff

@login_required
def show_dishes(id):
    form = Form()
    category = Category.query.get(id)
    return render_template('dishes/show_dishes.html',category=category,form=form)

@login_required
def add_dish():
    form = Form()
    categories = Category.query.all()
    if request.method == 'POST':
        new_dish = Dish(
            name = form.name.data,
            price = form.price.data,
            description = form.description.data,
            image = form.image.data, 
            is_gluten_free = form.is_gluten_free.data,
            is_vegeterian = form.is_vegeterian.data,
            category_id = request.form['category']
        )
        db.session.add(new_dish)
        db.session.commit()
        return redirect(url_for('category.menu'))
    return is_staff('dishes/add_dish.html',form=form,category=categories)

@login_required
def dish_management():
    categories = Category.query.all()
    return is_staff('dishes/dish_management.html',category=categories)

@login_required
def edit_dish(id):
    form = Form()
    dish = Dish.query.get(id)
    categories = Category.query.all()
    if request.method == 'POST':
        dish.name = form.name.data
        dish.price = form.price.data
        dish.description = form.description.data
        dish.image = form.image.data 
        dish.is_gluten_free = form.is_gluten_free.data
        dish.is_vegeterian = form.is_vegeterian.data
        dish.category_id = request.form['category']
        db.session.commit()
        return redirect(url_for('dish.dish_management'))
    return is_staff('dishes/edit_dish.html',dish=dish,category=categories,form=form)

@login_required
def delete_dish(id):
    dish = Dish.query.get(id)
    if request.method == 'POST':
        db.session.delete(dish)
        db.session.commit()
        return redirect(url_for('dish.dish_management'))
    return is_staff('dishes/delete_dish.html',dish=dish)
