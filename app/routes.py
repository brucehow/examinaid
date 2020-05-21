from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegisterForm, TestForm, MultiTestQuestion, ShortTestQuestion, OpenTestQuestion

from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
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
@login_required
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
@login_required
def newtest():
    print(listdir()) # Check our working directory - turns out it's one higher than expected
    file = open("app/questions/cits3403_1.json")
    data = load(file)
    return render_template('test_template.html', title="{} - New Test".format(data["unitName"]),
                            unit="{}: {}".format(data["unitCode"], data["unitName"]), questions=data["questions"], unitCode=data["unitCode"],
                            questionset='{}_{}'.format(data["unitCode"].lower(), data["testNumber"]))

# Add Questions function using JSON creation
@app.route('/addmultiq', methods=['GET', 'POST'])
def addmultiq():
    form = MultiTestQuestion()
    ##for relative file location
    dirname = path.dirname(__file__)
    dictionary = {
      "unitCode" : form.unitCode.data,
      "unitName": form.unitName.data,
      "testNumber": form.testNumber.data,
      "totalMarks": form.totalMarks.data,
      "questions": [
        {
          "questionNumber": 1,
          "marks" : form.marks1.data,
          "prompt": form.prompt1.data,
          "answer": form.answer1.data,
          "questionType": "multipleChoice",
          "totalOptions": form.options1.data
        },
        {
          "questionNumber": 2,
          "marks" : form.marks2.data,
          "prompt": form.prompt2.data,
          "answer": form.answer2.data,
          "questionType": "multipleChoice",
          "totalOptions": form.options2.data
        },
        {
          "questionNumber": 3,
          "marks" : form.marks3.data,
          "prompt": form.prompt3.data,
          "answer": form.answer3.data,
          "questionType": "multipleChoice",
          "totalOptions": form.options3.data
        },
        {
          "questionNumber": 4,
          "marks" : form.marks4.data,
          "prompt": form.prompt4.data,
          "answer": form.answer4.data,
          "questionType": "multipleChoice",
          "totalOptions": form.options4.data
        },
        {
          "questionNumber": 5,
          "marks" : form.marks5.data,
          "prompt": form.prompt5.data,
          "answer": form.answer5.data,
          "questionType": "multipleChoice",
          "totalOptions": form.options5.data
        },
                {
          "questionNumber": 6,
          "marks" : form.marks6.data,
          "prompt": form.prompt6.data,
          "answer": form.answer6.data,
          "questionType": "multipleChoice",
          "totalOptions": form.options6.data
        },
        {
          "questionNumber": 7,
          "marks" : form.marks7.data,
          "prompt": form.prompt7.data,
          "answer": form.answer7.data,
          "questionType": "multipleChoice",
          "totalOptions": form.options7.data
        },
        {
          "questionNumber": 8,
          "marks" : form.marks8.data,
          "prompt": form.prompt8.data,
          "answer": form.answer8.data,
          "questionType": "multipleChoice",
          "totalOptions": form.options8.data
        },
        {
          "questionNumber": 9,
          "marks" : form.marks9.data,
          "prompt": form.prompt9.data,
          "answer": form.answer9.data,
          "questionType": "multipleChoice",
          "totalOptions": form.options9.data
        },
        {
          "questionNumber": 10,
          "marks" : form.marks10.data,
          "prompt": form.prompt10.data,
          "answer": form.answer10.data,
          "questionType": "multipleChoice",
          "totalOptions": form.options10.data
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

@app.route('/addshortq', methods=['GET', 'POST'])
def addshortq():
    form = ShortTestQuestion()
    ##for relative file location
    dirname = path.dirname(__file__)
    dictionary = {
      "unitCode" : form.unitCode.data,
      "unitName": form.unitName.data,
      "testNumber": form.testNumber.data,
      "totalMarks": form.totalMarks.data,
      "questions": [
        {
          "questionNumber": 1,
          "marks" : form.marks1.data,
          "prompt": form.prompt1.data,
          "answer": form.answer1.data,
          "questionType": "shortAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 2,
          "marks" : form.marks2.data,
          "prompt": form.prompt2.data,
          "answer": form.answer2.data,
          "questionType": "shortAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 3,
          "marks" : form.marks3.data,
          "prompt": form.prompt3.data,
          "answer": form.answer3.data,
          "questionType": "shortAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 4,
          "marks" : form.marks4.data,
          "prompt": form.prompt4.data,
          "answer": form.answer4.data,
          "questionType": "shortAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 5,
          "marks" : form.marks5.data,
          "prompt": form.prompt5.data,
          "answer": form.answer5.data,
          "questionType": "shortAnswer",
          "totalOptions": None
        },
                {
          "questionNumber": 6,
          "marks" : form.marks6.data,
          "prompt": form.prompt6.data,
          "answer": form.answer6.data,
          "questionType": "shortAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 7,
          "marks" : form.marks7.data,
          "prompt": form.prompt7.data,
          "answer": form.answer7.data,
          "questionType": "shortAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 8,
          "marks" : form.marks8.data,
          "prompt": form.prompt8.data,
          "answer": form.answer8.data,
          "questionType": "shortAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 9,
          "marks" : form.marks9.data,
          "prompt": form.prompt9.data,
          "answer": form.answer9.data,
          "questionType": "shortAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 10,
          "marks" : form.marks10.data,
          "prompt": form.prompt10.data,
          "answer": form.answer10.data,
          "questionType": "shortAnswer",
          "totalOptions": None
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
    return render_template("tests/addshortq_template.html", title="Add Short Questions", form=form)
    


    
# The actual unique test page itself.
@app.route('/test/<questionset>')
@login_required
def test(questionset):
    questionSetPath = "app/questions/" + questionset + ".json"
    file = open(questionSetPath)
    data = load(file)
    return render_template('test_template.html', title="{} - New Test".format(data["unitName"]),
                            unit="{}: {}".format(data["unitCode"], data["unitName"]), questions=data["questions"], unitCode=data["unitCode"],
                            questionset=questionset)

# After a test is submitted
@app.route('/submit/', methods=['POST'])
@login_required
def submit():
    data = request.form
    print(data)
    flash("Test submitted!")
    return redirect(url_for('userprofile'))
