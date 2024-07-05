from flask import Flask, render_template, request
from data import Database

app = Flask(__name__)
db = Database()
@app.route("/")
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/perform_registration', methods=['post'])
def perform_registration():
    name = request.form.get('user_name')                  # for recieving the data by post method
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = db.insert(name,email,password)

    if response:
        return render_template('login.html', message='Registration Successful, Kindly Login to Proceed')
    else:
        return render_template('registration.html', message='Email Already Exists')

app.run(debug=True)