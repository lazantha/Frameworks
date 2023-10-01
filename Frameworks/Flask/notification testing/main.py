from flask import Flask, render_template, request, make_response,session,flash
from forms import LogIn
from database import Mysql
from datetime import date
import pdfkit

# Set the path to wkhtmltopdf executable


app=Flask(__name__)
app.config['SECRET_KEY']='key'
pdfkit_config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
app.config['PDFKIT_CONFIG'] = pdfkit_config


@app.route('/pdf',methods=['POST','GET'])
def pdf():
    if request.method=='GET':
        fname=request.args.get('fname')
        lname=request.args.get('lname')
        email=request.args.get('email')
        rendered = render_template('pdf.html',fname=fname,lname=lname)
        pdf = pdfkit.from_string(rendered, False)
        response = make_response(pdf)
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
        return response


@app.route('/report',methods=['POST','GET'])
def report():

        # if 'action' in request.args:
        #     rendered =render_template('report.html')
        #     pdf = pdfkit.from_string(rendered, False)
        #     response = make_response(pdf)
        #     response.headers['Content-Type'] = 'application/pdf'
        #     response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
        #     return response

    return render_template('report.html')







@app.route('/dateTime',methods=['GET','POST'])
def dateTime():

    
    new_date = request.args.get('new_date')
    print("Received Date:", new_date)

    if new_date:
        year = new_date.split('-')[0]
        print("Year:", year)
    else:
        print("Year: Date parameter not provided")

    return render_template('date.html')



@app.route('/ajax',methods=['GET','POST'])
def ajax():
    name = request.args.get('name')
    dep = request.args.get('dep')
    print(name)
    print(dep)


    return render_template('ajax.html')



if __name__=='__main__':
	app.run(debug=True)
