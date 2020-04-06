from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegisterForm

@app.route("/")
@app.route("/landing")
def landing():
    return render_template("landing.html")

@app.route("/index")
def index():
    site_title = "Site Title"
    welcome_string = ""
    return render_template("index.html", welcome_string=welcome_string, site_title=site_title)

@app.route("/about")
def about():
    name = "Nobody"
    return render_template("about.html", name=name)

@app.route("/login", methods = ["GET", "POST"])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(loginForm.username.data, loginForm.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', loginForm=loginForm)

@app.route('/register', methods=['GET', 'POST'])
def register():
    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        flash('Registration requested for user {}, remember_me={}'.format(registerForm.username.data, registerForm.remember_me.data))
        return redirect('/login')
    return render_template('register.html', title='Register', registerForm=registerForm)

