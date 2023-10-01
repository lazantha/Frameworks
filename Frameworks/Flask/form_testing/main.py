from flask import Flask, render_template,request

app = Flask(__name__)
@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        print(first_name)
    else:
        value = request.args.get('value')
        if value:
            print(value)
        else:
            print("Not found")
        
    return render_template('index.html')
