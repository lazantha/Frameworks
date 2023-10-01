from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,BooleanField,SelectField
from wtforms.validators import DataRequired,Length,Email,EqualTo


#registration
class UserForm(FlaskForm):
	first_name=StringField("Frist Name",validators=[DataRequired(),Length(min=2,max=20)])
	last_name=StringField("Last Name",validators=[DataRequired()])
	password=PasswordField("Enter Password",validators=[DataRequired()])
	confirm_pass=PasswordField("Confirm Passowrd",validators=[DataRequired(),EqualTo('password')])
	email=StringField('Email',validators=[DataRequired()])
	submit=SubmitField("Save")

#log in 
class UserLog(FlaskForm):
	
	email=StringField('Email',validators=[DataRequired()])
	password=PasswordField("Enter Password",validators=[DataRequired()])
	dep=SelectField("Select Department",choices=['IT','English','Management'])
	submit=SubmitField("Log In")

