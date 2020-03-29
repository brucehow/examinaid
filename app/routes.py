from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

@app.route("/")
@app.route("/main")
def main():
    return render_template("main.html")

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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)