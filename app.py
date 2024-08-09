from flask import Flask, render_template, request, redirect
from data import Database
import api

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
    name = request.form.get('user_name')                  # for receiving the data by post method
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = db.insert(name, email, password)

    if response:
        return render_template('login.html', message='Registration Successful, Kindly Login to Proceed')
    else:
        return render_template('registration.html', message='Email Already Exists')


@app.route('/perform_login', methods=['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')

    response = db.search(email, password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html', message='Incorrect Email/Password')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/ner')
def ner():
    return render_template('ner.html')


@app.route('/perform_ner')
def perform_ner():
    text = request.form.get('ner_text')
    response = api.ner(text)
    print(response)
    return "Something"


app.run(debug=True, port=4000)
