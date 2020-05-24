from app import app, db
from flask import render_template, flash, redirect, url_for, request

from app.forms import LoginForm, RegisterForm, TestForm, ResetPasswordForm, MultiTestQuestion, ShortTestQuestion, OpenTestQuestion
from app.unitJSON import add_test, get_tests, get_all, remove_unit, remove_test
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, db
from werkzeug.urls import url_parse

from json import load, dumps
from os import listdir, path # To debug file paths
from app.unitJSON import get_all

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

@app.route("/attempts")
def attempts():
    return render_template("attempts.html", title="Previous Attempts")

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", title="Quiz")

@app.route("/newtest", methods = ["GET", "POST"])
def newtest():
    form = TestForm()
    if form.validate_on_submit():
      questionset = form.questionset.data
      return redirect(url_for("test", questionset=questionset))
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

# Admin mark tests
@app.route('/marktests')
@login_required
def marktests():
    if not current_user.check_admin(): # Student logins cannot access this page
        return redirect(url_for('userprofile'))
    else:
        return render_template('marktests.html', title="Mark Completed Tests")

# Admin manage tests
@app.route('/managetests')
@login_required
def managetests():
    if not current_user.check_admin(): # Student logins cannot access this page
        return redirect(url_for('userprofile'))
    else:
        tests = get_all("app/questions/units.json")
        questionSets = []
        for unit in tests:
            for qset in tests[unit]:
                filepath = "app/questions/{}_{}.json".format(unit.lower(), qset)
                questionSet = load(open(filepath))s
                numq = 0
                for question in questionSet["questions"]:
                    numq += 1
                thisSet = {
                    "unitCode": questionSet["unitCode"],
                    "unitName": questionSet["unitName"],
                    "testNumber": questionSet["testNumber"],
                    "totalMarks": questionSet["totalMarks"],
                    "questions": numq
                }
                questionSets.append(thisSet)
        return render_template('manage/tests.html', title="Manage Tests", sets=questionSets)

# Add Questions function using JSON creation
@app.route('/managetests/add_multiq', methods=['GET', 'POST'])
@login_required
def add_multiq():
  if current_user.check_admin():
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
      if add_test(form.unitCode.data, form.testNumber.data) == -1:
        flash('Error: Test already exists!')
        return redirect(url_for('userprofile'))
      else:
        with open(path.join(dirname, "questions/" + form.unitCode.data.lower() + "_" + str(form.testNumber.data)  + ".json"), "w") as outfile:
          outfile.write(json_object)
          flash('Questions added!')
          return redirect(url_for('userprofile'))
  else:
    flash('Not an admin: Please contact your supervisor')
    return redirect(url_for('userprofile'))
  return render_template("tests/addmultiq_template.html", title="Add MultipleChoice Questions", form=form)

@app.route('/managetests/add_shortq', methods=['GET', 'POST'])
@login_required
def add_shortq():
  if current_user.check_admin():
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
      if add_test(form.unitCode.data, form.testNumber.data) == -1:
        flash('Error: Test already exists!')
        return redirect(url_for('userprofile'))
      else:
        with open(path.join(dirname, "questions/" + form.unitCode.data.lower() + "_" + str(form.testNumber.data)  + ".json"), "w") as outfile:
          outfile.write(json_object)
          flash('Questions added!')
          return redirect(url_for('userprofile'))
  else:
    flash('Not an admin: Please contact your supervisor')
    return redirect(url_for('userprofile'))

    #change questions/test.json to be an actual variable for file storage and loading


  return render_template("tests/addshortq_template.html", title="Add Short Questions", form=form)

@app.route('/managetests/add_openq', methods=['GET', 'POST'])
@login_required
def add_openq():
  if current_user.check_admin():
    form = OpenTestQuestion()
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
          "answer": None,
          "questionType": "openAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 2,
          "marks" : form.marks2.data,
          "prompt": form.prompt2.data,
          "answer": None,
          "questionType": "openAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 3,
          "marks" : form.marks3.data,
          "prompt": form.prompt3.data,
          "answer": None,
          "questionType": "openAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 4,
          "marks" : form.marks4.data,
          "prompt": form.prompt4.data,
          "answer": None,
          "questionType": "openAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 5,
          "marks" : form.marks5.data,
          "prompt": form.prompt5.data,
          "answer": None,
          "questionType": "openAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 6,
          "marks" : form.marks6.data,
          "prompt": form.prompt6.data,
          "answer": None,
          "questionType": "openAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 7,
          "marks" : form.marks7.data,
          "prompt": form.prompt7.data,
          "answer": None,
          "questionType": "openAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 8,
          "marks" : form.marks8.data,
          "prompt": form.prompt8.data,
          "answer": None,
          "questionType": "openAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 9,
          "marks" : form.marks9.data,
          "prompt": form.prompt9.data,
          "answer": None,
          "questionType": "openAnswer",
          "totalOptions": None
        },
        {
          "questionNumber": 10,
          "marks" : form.marks10.data,
          "prompt": form.prompt10.data,
          "answer": None,
          "questionType": "openAnswer",
          "totalOptions": None
        }
      ]
    }
    ##dumps for 4 items, change indent variable if there's more items required
    json_object = dumps(dictionary, indent = 4)
    
    if form.validate_on_submit():
      if add_test(form.unitCode.data, form.testNumber.data) == -1:
        flash('Error: Test already exists!')
        return redirect(url_for('userprofile'))
      else:
        with open(path.join(dirname, "questions/" + form.unitCode.data.lower() + "_" + str(form.testNumber.data)  + ".json"), "w") as outfile:
          outfile.write(json_object)
          flash('Questions added!')
          return redirect(url_for('userprofile'))
  else:
    flash('Not an admin: Please contact your supervisor')
    return redirect(url_for('userprofile'))
  return render_template("tests/addopenq_template.html", title="Add Open Questions", form=form)



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
@app.route('/manageusers')
@login_required
def manageusers():
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

@app.route('/manageusers/remove/<user_id>')
@login_required
def remove(user_id):
    user_id = int(user_id) # Manual cast, the id comes in initially as a string
    print("Attempting to remove user with ID {}.".format(user_id))
    users = User.query.all()
    for user in users:
        if (user_id == user.id):
            if (user == current_user):
                print("You removed yourself. Oh wait - you can't.")
                break
            else:
                db.session.delete(user)
                db.session.commit()
                print("User {} has been removed.".format(user.username))
                break
    return redirect(url_for('manageusers'))

@app.route('/manageusers/adduser', methods=['POST'])
@login_required
def adduser():
    data = request.form
    if data:
        print(data["username"], data["email"], data["password"])
        if (data["username"] == '') or (data["email"] == ''):
            print("Cannot add a user without both a username and an email.")
        else:
            user = User(username=data["username"], email=data["email"])
            if (data["password"] is not None):
              print("Password specified.")
              user.set_password(data["password"])
            else:
              print("Password not specified.")
              user.set_password("password1")
            db.session.add(user)
            db.session.commit()
    else:
        print("No data")
    return redirect(url_for('manageusers'))

@app.route('/changepassword', methods=['GET', 'POST'])
@login_required
def changepassword():
    form = ResetPasswordForm()
    if form.validate_on_submit():
        current_user.set_password(form.newPassword.data)
        db.session.commit()
        print("Password for {} updated successfully.".format(current_user.username))
        return redirect(url_for('userprofile'))
    return render_template("changepassword.html", title="Change Password", resetPasswordForm=form)