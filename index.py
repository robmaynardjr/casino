from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def casino():
    return render_template('login.html')

@app.route('/signup.html')
def sign_up():
    return render_template('signup.html')