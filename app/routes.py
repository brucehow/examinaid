from app import app
from flask import render_template

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