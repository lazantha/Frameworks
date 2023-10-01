from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    fname = lname = ""

    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        print("IN POST: ", fname)

        # Process the data and send a JSON response
        response_data = {'fname': fname, 'lname': lname}
        return jsonify(response_data)

    return render_template('index.html', fname=fname, lname=lname)

if __name__ == '__main__':
    app.run(debug=True)
