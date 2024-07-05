from flask import Flask, render_template, request

app = Flask(__name__)

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
    return name + " " + email + " " + password

app.run(debug=True)