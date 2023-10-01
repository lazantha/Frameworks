from flask import Flask,render_template,url_for,request,redirect
from allForms import UserLog,UserForm


app=Flask(__name__)
app.config['SECRET_KEY']='Key'


@app.route('/')
def index():
	newUser=UserLog()


	return render_template('index.html',form=newUser)


@app.route('/log')
def reg():
	newForm=UserForm()
	return render_template('log.html',form=newForm)