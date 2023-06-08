from flask import render_template,request,redirect,url_for
from flask_login import login_required
from db import db
from models.category import Category
from models.form import Form
from utils import is_staff

@login_required
def menu():
    categories = Category.query.all()
    return render_template('categories/menu.html',categories=categories)

@login_required
def category_management():
    categories = Category.query.all()
    return is_staff('categories/category_management.html', categories)

@login_required
def edit_category(id):
    category = Category.query.get(id)
    form = Form()
    if request.method == 'POST':
        category.name = form.name.data
        category.image = form.image.data
        db.session.commit()
        return redirect(url_for('category.category_management'))
    return is_staff('categories/edit_category.html',category = category,form = form)

@login_required
def delete_category(id):
    category = Category.query.get(id)
    if request.method == 'POST':
        db.session.delete(category)
        db.session.commit()
        return redirect(url_for('category.category_management'))
    return is_staff('categories/delete_category.html',category=category)

@login_required
def add_category():
    form = Form()
    if request.method == 'POST':
        new_category = Category(
            name = form.name.data,
            image = form.image.data 
        )
        db.session.add(new_category)
        db.session.commit()
        return redirect(url_for('category.menu'))
    return is_staff('categories/add_category.html',form = form)