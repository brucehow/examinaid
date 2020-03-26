from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    site_title = "General Kenobi"
    welcome_string = "Hello World! Welcome to this skeleton of an application."
    return render_template("index.html", welcome_string=welcome_string, site_title=site_title)

@app.route("/about")
def about():
    name = "Nobody"
    return render_template("about.html", name=name)