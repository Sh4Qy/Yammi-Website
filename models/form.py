from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,BooleanField,TextAreaField,IntegerField,PasswordField
from wtforms.validators import DataRequired,Email

class Form(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    new_password = StringField("Password",validators=[DataRequired()])
    first_name = StringField("First Name",validators=[DataRequired()])
    last_name = StringField("Last Name",validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    name = StringField("Name",validators=[DataRequired()])
    price = IntegerField("Price")
    description = StringField("About the dish")
    image = StringField("Image",validators=[DataRequired()])
    is_gluten_free = BooleanField("Gluten Free")
    is_vegeterian = BooleanField("Vegeterian")
    amount = SelectField("Amount",choices=[(num,num) for num in range(1,11)])
    address = StringField("Address",validators=[DataRequired()])
    comment = TextAreaField("Special Request",validators=[DataRequired()])

class EmailForm(FlaskForm):
    email = StringField("Email",validators=[Email("Please enter a valid email address.")])