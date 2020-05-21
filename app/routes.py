from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegisterForm, TestForm, TestQuestion

from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, db
from werkzeug.urls import url_parse

from json import load, dumps
from os import listdir, path # To debug file paths

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
@login_required
def userprofile():
    return render_template("userprofile.html", title="My Profile")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", title="Quiz")

# Test selection page; could be phased into the student profile
@app.route("/newtest")
def newtest2():
    form = TestForm()
    return render_template("tests/newtest.html", title="Start New Test", form=form)


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
        # Did the user get directed here after trying to access a protected page?
        next_page = request.args.get('next')
        # If not, set the next page to the index.
        # The second check below is to prevent malicious intent by checking that the netlog component has been set, which is only true for relative URLs.
        if (not next_page) or (url_parse(next_page).netloc != ''):
            next_page = url_for('userprofile')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', loginForm=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
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
        flash('Registered successfully!')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

# Add Questions function using JSON creation
@app.route('/addQuestions', methods=['GET', 'POST'])
def addQuestions():
    form = TestQuestion()
    ##for relative file location
    dirname = path.dirname(__file__)
    dictionary = {
      "unitCode" : form.unitCode.data,
      "unitName": form.unitName.data,
      "testNumber": form.testNumber.data,
      "questions": [
        {
          "questionNumber": form.questionNumber.data,
          "prompt": form.prompt.data,
          "answer": form.answer.data,
          "questionType": form.questionType.data,
          "totalOptions": [form.options.data]
        }
      ]
    }
    ##dumps for 4 items, change indent variable if there's more items required
    json_object = dumps(dictionary, indent = 4)
    
    if form.validate_on_submit():
    #change questions/test.json to be an actual variable for file storage and loading
      with open(path.join(dirname, "questions/test.json"), "w") as outfile:
        outfile.write(json_object)
        flash('Questions added!')
        return redirect(url_for('userprofile'))
    return render_template("tests/AddQuestion_template.html", title="Add Questions", form=form)

    
# The actual unique test page itself.
@app.route('/test/<questionset>')
@login_required
def test(questionset):
    print(listdir()) # Check our working directory - turns out it's one higher than expected
    questionSetPath = "app/questions/" + questionset + ".json"
    file = open(questionSetPath)
    data = load(file)
    return render_template('tests/test_template.html', title="{} - New Test".format(data["unitName"]),
                            unit="{}: {}".format(data["unitCode"], data["unitName"]), questions=data["questions"], unitCode=data["unitCode"],
                            questionset=questionset)

# After a test is submitted
@app.route('/submit/', methods=['POST'])
@login_required
def submit():
    data = request.form
    print(data)
    return redirect(url_for('userprofile'))

# Admin manage student logins
@app.route('/managestudents')
@login_required
def managestudents():
    if not current_user.check_admin(): # Student logins cannot access this page
        return redirect(url_for('userprofile'))
    else:
        users = User.query.all()
        num_admins = 0
        num_students = 0
        for user in users:
            if user.check_admin():
                num_admins += 1
            else:
                num_students += 1
        return render_template('manage/students.html', num_users=len(users), num_admins=num_admins, num_students=num_students, users=users)

@app.route('/managestudents/remove/<user_id>')
@login_required
def remove(user_id):
    user_id = int(user_id) # Manual cast, the id comes in initially as a string
    print("Attempting to remove user with ID {}.".format(user_id))
    users = User.query.all()
    for user in users:
        if (user_id == user.id):
            if (user != current_user):
                print("You removed yourself. Oh wait - you can't.")
                break
            else:
                db.session.delete(user)
                db.session.commit()
                print("User {} has been removed.".format(user.username))
                break
    return redirect(url_for('managestudents'))