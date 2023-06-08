from flask import render_template,request,redirect,url_for,flash
from db import db
from models.form import Form,EmailForm
from models.user import User
from models.cart import Cart
from flask_login import login_user,login_required,logout_user,current_user
from sqlalchemy.exc import IntegrityError
from utils import is_staff


def main():
    return render_template('users/main.html')

def register():
    form = Form()
    email_form = EmailForm()
    if request.method == 'POST' and email_form.validate_on_submit():
        if any([l.isnumeric() for l in form.first_name.data]):
            flash('You cannot enter numbers in your First Name','first_name error')
            return redirect(url_for('user.register'))
        if any([l.isnumeric() for l in form.last_name.data]):
            flash('You cannot enter numbers in your Last Name','last_name error')
            return redirect(url_for('user.register'))
        new_user = User(
            username = form.username.data,
            password = form.password.data,
            first_name = form.first_name.data,
            last_name = form.last_name.data,
        )
        try:
            db.session.add(new_user)
            db.session.commit()
        except IntegrityError:
            flash('This username is already taken','username error')
            return redirect(url_for('user.register'))
        if User.query.filter_by(email = email_form.email.data).first() == None:
            new_user.email = email_form.email.data
            db.session.commit()
        else:
            db.session.delete(new_user)
            db.session.commit()
            flash('There is an account with that email address','email error')
            return redirect(url_for('user.register'))
        new_cart = Cart(user_id = new_user.id)
        db.session.add(new_cart)
        db.session.commit()
        return redirect(url_for('user.sign_in'))
    else:
        return render_template('users/register.html',form=form,email_form=email_form)

def sign_in():
    form = Form()
    if request.method == 'POST':
        user = User.query.filter_by(username=form.username.data).first()
        if user != None:
            if form.password.data == user.password:
                login_user(user,remember=form.remember_me.data)
                flash('You have been successfully logged in.','success')
                return redirect(url_for('category.menu'))
            else:
                flash('The password is incorrect.','error')
        else:
            flash('No user found with this username.','error')
    return render_template('users/sign_in.html',form=form)

@login_required
def add_admin():
    users = User.query.filter_by(is_staff = False).all()
    if request.method == 'POST':
        user = User.query.get(request.form['user_id'])
        user.is_staff = True
        db.session.commit()
        return redirect(url_for('user.add_admin'))
    return is_staff('users/add_admin.html',users=users)

@login_required
def log_out():
    logout_user()
    return redirect(url_for('user.main'))
    

@login_required
def edit_profile():
    email_form = EmailForm()
    form = Form()
    if request.method == 'POST' and email_form.validate_on_submit():
        if any([l.isnumeric() for l in form.first_name.data]):
            flash('You cannot enter numbers in your First Name','first_name error')
            return redirect(url_for('user.edit_profile'))
        if any([l.isnumeric() for l in form.last_name.data]):
            flash('You cannot enter numbers in your Last Name','last_name error')
            return redirect(url_for('user.edit_profile'))
        if (User.query.filter_by(username = form.username.data).first() != None 
            and current_user.username != form.username.data):
            flash('This username is already taken','username error')
            return redirect(url_for('user.edit_profile'))
        if (User.query.filter_by(email = email_form.email.data).first() != None 
            and current_user.email != email_form.email.data):
            flash('There is an account with that email address','email error')
            return redirect(url_for('user.edit_profile'))
        current_user.username = form.username.data
        current_user.password = form.new_password.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = email_form.email.data
        db.session.commit()
        return redirect(url_for('category.menu'))
    else:
        return render_template('users/edit_profile.html',form=form,email_form=email_form)
