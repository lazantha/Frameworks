from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField,DateField,PasswordField
from flask_wtf.file import FileField

class Log(FlaskForm):

    name = StringField("Name: ")
    password = PasswordField()
    submit = SubmitField("Submit")
    possition = SelectField("Posstion: ", choices=['OFFICE', 'HOD'])
    department = SelectField("Department: ", choices=['IT', 'ACCOUNTANCY', 'MANAGEMENT', 'TOURISM'])


class UserSignUp(FlaskForm):
    first_name=StringField("First Name: ")
    last_name=StringField("Last Name: ")
    department=SelectField("Department: ")
    email=StringField("Email: ")
    password=StringField("Password: ")
    confirm_password=StringField("Confirm Password: ")
    submit=SubmitField("Submit")
    
    # pic=FileField('Avatar', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])


class AdminSign(FlaskForm):
    first_name=StringField("First Name")
    last_name=StringField("First Name")
    pic=FileField('Red Book')
    submit=SubmitField("Submit")

class DateForm(FlaskForm):
    start_date=DateField("Start Date")
    end_date=DateField("End Date")
    submit=SubmitField("Submit")

class Images(FlaskForm):
    pic=FileField("Enter File")
    submit=SubmitField("Submit")