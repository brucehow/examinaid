from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField, SelectField, FieldList
from wtforms.validators import DataRequired, InputRequired
from flask_login import current_user
from app.unitJSON import get_all

# The following validators and User object are only required for the Register form.
from wtforms.validators import ValidationError, Email, EqualTo
from app.models import User

# This is a class inheritance definition; this class inherits properties of FlaskForm. See: https://docs.python.org/3/tutorial/classes.html#class-definition-syntax
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()]) # The email validator checks that the user has entered an email address
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    # WTForms takes the following validators and adds them to the stock validators, and will do so for any function with the name "validate_<something>".
    def validate_username(self, username): # Checks if the username is already taken
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.') # This message will be displayed next to the username field for the user to see.
    
    def validate_email(self, email): # Checks if there is already an account with the current email
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

# Potential form for the unit test selection
class TestForm(FlaskForm):
    questionset = SelectField('Question Set', [DataRequired()], choices = [("{}_{}".format(unit.lower(), setnumber), "{} Set {}".format(unit, setnumber)) for unit in get_all("app/questions/units.json") for setnumber in get_all("app/questions/units.json")[unit]]) # ('cits1401_1','CITS1401 Set 1')
    submit = SubmitField('Start Test')

class ManualMarkForm(FlaskForm):
    mark1 = IntegerField('Mark', validators=[InputRequired(message="Invalid Marks Value")])
    mark2 = IntegerField('Mark', validators=[InputRequired(message="Invalid Marks Value")])
    mark3 = IntegerField('Mark', validators=[InputRequired(message="Invalid Marks Value")])
    mark4 = IntegerField('Mark', validators=[InputRequired(message="Invalid Marks Value")])
    mark5 = IntegerField('Mark', validators=[InputRequired(message="Invalid Marks Value")])
    mark6 = IntegerField('Mark', validators=[InputRequired(message="Invalid Marks Value")])
    mark7 = IntegerField('Mark', validators=[InputRequired(message="Invalid Marks Value")])
    mark8 = IntegerField('Mark', validators=[InputRequired(message="Invalid Marks Value")])
    mark9 = IntegerField('Mark', validators=[InputRequired(message="Invalid Marks Value")])
    mark10 = IntegerField('Mark', validators=[InputRequired(message="Invalid Marks Value")])

class MultiTestQuestion(FlaskForm):
    unitName = StringField('UnitName', validators=[DataRequired()])
    unitCode = StringField('UnitCode', validators=[DataRequired()])

    prompt1 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer1 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    options1 = FieldList(StringField('Options:'), min_entries=4)
    marks1 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt2 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer2 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    options2 = FieldList(StringField('Options:'), min_entries=4)
    marks2 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt3 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer3 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    options3 = FieldList(StringField('Options:'), min_entries=4) 
    marks3 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt4 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer4 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    options4 = FieldList(StringField('Options:'), min_entries=4)
    marks4 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt5 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer5 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    options5 = FieldList(StringField('Options:'), min_entries=4) 
    marks5 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt6 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer6 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    options6 = FieldList(StringField('Options:'), min_entries=4)
    marks6 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt7 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer7 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    options7 = FieldList(StringField('Options:'), min_entries=4) 
    marks7 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt8 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer8 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    options8 = FieldList(StringField('Options:'), min_entries=4) 
    marks8 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt9 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer9 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    options9 = FieldList(StringField('Options:'), min_entries=4) 
    marks9 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt10 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer10 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    options10 = FieldList(StringField('Options:'), min_entries=4) 
    marks10 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
class ShortTestQuestion(FlaskForm):
    unitName = StringField('UnitName', validators=[DataRequired()])
    unitCode = StringField('UnitCode', validators=[DataRequired()])

    prompt1 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer1 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    marks1 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt2 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer2 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    marks2 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt3 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer3 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    marks3 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt4 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer4 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    marks4 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt5 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer5 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    marks5 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt6 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer6 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    marks6 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt7 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer7 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    marks7 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt8 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer8 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    marks8 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt9 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer9 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    marks9 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt10 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    answer10 = StringField('Answer', validators=[DataRequired(message="Answer Field Required")])
    marks10 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
class OpenTestQuestion(FlaskForm):
    unitName = StringField('UnitName', validators=[DataRequired()])
    unitCode = StringField('UnitCode', validators=[DataRequired()])

    prompt1 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    marks1 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])

    prompt2 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    marks2 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt3 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    marks3 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])

    prompt4 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    marks4 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt5 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    marks5 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])

    prompt6 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    marks6 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])

    prompt7 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    marks7 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])

    prompt8 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    marks8 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt9 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    marks9 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])
    
    prompt10 = StringField('Prompt', validators=[DataRequired(message="Prompt Field Required")])
    marks10 = IntegerField('Marks', validators=[DataRequired(message="Invalid Marks Value")])

# Form to reset user password
class ResetPasswordForm(FlaskForm):
    email = StringField('Current Email', validators=[DataRequired(), Email()])
    currentPassword = PasswordField('Current Password', validators=[DataRequired()])
    newPassword = PasswordField('New Password', validators=[DataRequired()])
    repeatPassword = PasswordField('Repeat New Password', validators=[DataRequired(), EqualTo('newPassword')])
    submit = SubmitField('Change Password')

    def validate_email(self, email):
        if (current_user.email != email.data):
            raise ValidationError("Incorrect email.")

    def validate_currentPassword(self, currentPassword):
        if (not current_user.check_password(currentPassword.data)):
            raise ValidationError("Current password is incorrect.")

    def validate_newPassword(self, newPassword):
        if (newPassword.data == self.currentPassword.data):
            raise ValidationError("New password must be different to current password.")
