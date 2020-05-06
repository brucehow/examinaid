from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegisterForm, TestForm

from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

from json import load
from os import listdir # To debug file paths

@app.route("/")
@app.route("/index")
def index():
    welcome_string = ""
    return render_template("index.html", welcome_string=welcome_string, title="Home")

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/contact")
def contact():
    return render_template("contact.html", title="Contact")

@app.route("/userprofile")
def userprofile():
    return render_template("userprofile.html", title="My Profile")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", title="Quiz")

@app.route("/newtest2")
def newtest2():
    form = TestForm()
    return render_template("newtest.html", title="Start New Test", form=form)


@app.route("/login", methods = ["GET", "POST"])
def login():
    # If there is a user currently logged in, return user to index page
    if (current_user.is_authenticated):
        return redirect(url_for('userprofile'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if (user is None) or (not user.check_password(form.password.data)): # Login unsuccessful
            flash("Invalid username or password.")
            return redirect(url_for('login'))
        # Otherwise the login was successful
        login_user(user, remember=form.remember_me.data)
        flash("Successfully logged in!")
        # Did the user get directed here after trying to access a protected page?
        next_page = request.args.get('next')
        # If not, set the next page to the index.
        # The second check below is to prevent malicious intent by checking that the netlog component has been set, which is only true for relative URLs.
        if (not next_page) or (url_parse(next_page).netloc != ''):
            next_page = url_for('userprofile')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', loginForm=form)

@app.route('/logout')
def logout():
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        # Add the user to the users database
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

# An example test form layout below
@app.route('/newtest')
def newtest():
    print(listdir()) # Check our working directory - turns out it's one higher than expected
    file = open("app/questions/example.json")
    data = load(file)
    return render_template('tests/test_template.html', unit="{}: {}".format(data["unitCode"], data["unitName"]), questions=data["questions"])