from flask import Flask, render_template, redirect, flash,session
from form import Log
from connection import MySql
from werkzeug.utils import secure_filename
from flask_mail import Mail,Message
import uuid
import os
from logger import logging
import mysql.connector
host='localhost'
user='root'
password=''
database='userinfor'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/',methods=['POST','GET'])
def index():
	form=Log()
	new_data=MySql(host,user,password,database,connection)
	if form.validate_on_submit():
		name=form.name.data
		password=form.password.data
		possition=form.possition.data
		session["user_name"]=name
		session['password']=password
		
		query="INERT INTO user (first_name,password,possition) VALUUES(%s,%s,%s);"
		data=(name,password,possition)
		new_data.table(query,data)


	return render_template('userlog.html',form=form)

@app.route('/sess')
def sess():
	new_data=MySql(host,user,password,database)
	query="SELECT * FROM users WHERE id=%s;"
	data=(1,)
	result=new_data.fetchOneForeing(query,data)
	print(result)


	
	








# @app.route('/', methods=['GET', 'POST'])
# def index():
	
#     new_data = MySql()
#     new_form = AdminSign()
#     if new_form.validate_on_submit():
#         first_name = new_form.first_name.data
#         last_name = new_form.last_name.data
#         id_card = new_form.pic.data
#         session['first_name']=first_name
#         session['last_name']=last_name

        
#         # Grab image name
        
#         img_name = secure_filename(id_card.filename)
        
#         uniq_name = str(uuid.uuid1()) + '_' + img_name

#         # Save image
#         save_path = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'], uniq_name)
#         id_card.save(save_path)

#         # Save to db
#         id_card = uniq_name
#         query="INSERT INTO images(image) VALUES(%s);"
#         values=(id_card,)
#         new_data.table(query,values,host,database,user)

#         flash("Upladed successfully And Mail sent !")
#         return redirect('/')
        

#     return render_template('index.html', form=new_form)


# @app.route('/display', methods=['GET', 'POST'])
# def display():
# 	new_data = MySql()
# 	if 'first_name' in session and 'last_name' in session:
# 		user_name=session['first_name']
# 		query="SELECT image FROM images ORDER BY id DESC"
# 		result=new_data.getData(query,host,database,user)
# 		cleaned_value = str(result.decode('utf-8'))

# 		logging.infor(cleaned_value)

# 	return render_template('display.html',user_name=user_name)


# @app.route('/user',methods=['GET','POST'])
# def user():
# 	form=UserSignUp()
# 	new_data = MySql()
# 	department_list=['IT','ACCOUNTENCY','MANAGEMENT','THM']
# 	form.department.choices=department_list
# 	if form.validate_on_submit():
# 		first_name=new_data.first_name.data
# 		last_name=new_data.last_name.data
# 		department=new_data.department.data
# 		email=new_data.email.data
# 		password=new_data.password.data
# 		confirm_password=new_data.confirm_password.data
# 		session['user_name']=first_name
# 		session['password']=password		
# 		return render_template('index.html')


# @app.route('/sessions')
# def sessions():
# 	if 'user_name' in session:
# 		return render_template('sessions.html')
# 	else:
# 		return "No values"
