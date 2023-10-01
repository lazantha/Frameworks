from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,DateField

class LogIn(FlaskForm):
	date=DateField()
	submit=SubmitField("Submit")
