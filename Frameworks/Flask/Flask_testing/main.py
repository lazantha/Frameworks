from flask import Flask,render_template,url_for,request,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)
@app.route('/')
def index():
	return render_template('index.html')
	
