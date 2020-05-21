from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, PasswordField, BooleanField, SubmitField, SelectField, FieldList
from wtforms.validators import DataRequired

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
    unit = SelectField('Unit', [DataRequired()], choices = [('python','CITS1401'),('dsa','CITS2200'),('ai','CITS3001')])
    testtype = SelectField('Assessment Type', [DataRequired()], choices = [('midsem','Mid-Semester'),('final','Final Examination')])

class MultiTestQuestion(FlaskForm):
    unitName = StringField('UnitName', validators=[DataRequired()])
    unitCode = StringField('UnitCode', validators=[DataRequired()])
    testNumber = IntegerField('TestName', validators=[DataRequired()])
    totalMarks = IntegerField('TotalMarks', validators=[DataRequired()])

    prompt1 = StringField('Prompt', validators=[DataRequired()])
    answer1 = StringField('Answer', validators=[DataRequired()])
    options1 = FieldList(StringField('Options:'), min_entries=4)
    marks1 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt2 = StringField('Prompt', validators=[DataRequired()])
    answer2 = StringField('Answer', validators=[DataRequired()])
    options2 = FieldList(StringField('Options:'), min_entries=4)
    marks2 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt3 = StringField('Prompt', validators=[DataRequired()])
    answer3 = StringField('Answer', validators=[DataRequired()])
    options3 = FieldList(StringField('Options:'), min_entries=4) 
    marks3 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt4 = StringField('Prompt', validators=[DataRequired()])
    answer4 = StringField('Answer', validators=[DataRequired()])
    options4 = FieldList(StringField('Options:'), min_entries=4)
    marks4 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt5 = StringField('Prompt', validators=[DataRequired()])
    answer5 = StringField('Answer', validators=[DataRequired()])
    options5 = FieldList(StringField('Options:'), min_entries=4) 
    marks5 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt6 = StringField('Prompt', validators=[DataRequired()])
    answer6 = StringField('Answer', validators=[DataRequired()])
    options6 = FieldList(StringField('Options:'), min_entries=4)
    marks6 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt7 = StringField('Prompt', validators=[DataRequired()])
    answer7 = StringField('Answer', validators=[DataRequired()])
    options7 = FieldList(StringField('Options:'), min_entries=4) 
    marks7 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt8 = StringField('Prompt', validators=[DataRequired()])
    answer8 = StringField('Answer', validators=[DataRequired()])
    options8 = FieldList(StringField('Options:'), min_entries=4) 
    marks8 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt9 = StringField('Prompt', validators=[DataRequired()])
    answer9 = StringField('Answer', validators=[DataRequired()])
    options9 = FieldList(StringField('Options:'), min_entries=4) 
    marks9 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt10 = StringField('Prompt', validators=[DataRequired()])
    answer10 = StringField('Answer', validators=[DataRequired()])
    options10 = FieldList(StringField('Options:'), min_entries=4) 
    marks10 = IntegerField('Marks', validators=[DataRequired()])
    

class ShortTestQuestion(FlaskForm):
    unitName = StringField('UnitName', validators=[DataRequired()])
    unitCode = StringField('UnitCode', validators=[DataRequired()])
    testNumber = IntegerField('TestName', validators=[DataRequired()])
    totalMarks = IntegerField('TotalMarks', validators=[DataRequired()])

    prompt1 = StringField('Prompt', validators=[DataRequired()])
    answer1 = StringField('Answer', validators=[DataRequired()])
    marks1 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt2 = StringField('Prompt', validators=[DataRequired()])
    answer2 = StringField('Answer', validators=[DataRequired()])
    marks2 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt3 = StringField('Prompt', validators=[DataRequired()])
    answer3 = StringField('Answer', validators=[DataRequired()])
    marks3 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt4 = StringField('Prompt', validators=[DataRequired()])
    answer4 = StringField('Answer', validators=[DataRequired()])
    marks4 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt5 = StringField('Prompt', validators=[DataRequired()])
    answer5 = StringField('Answer', validators=[DataRequired()])
    marks5 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt6 = StringField('Prompt', validators=[DataRequired()])
    answer6 = StringField('Answer', validators=[DataRequired()])
    marks6 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt7 = StringField('Prompt', validators=[DataRequired()])
    answer7 = StringField('Answer', validators=[DataRequired()])
    marks7 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt8 = StringField('Prompt', validators=[DataRequired()])
    answer8 = StringField('Answer', validators=[DataRequired()])
    marks8 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt9 = StringField('Prompt', validators=[DataRequired()])
    answer9 = StringField('Answer', validators=[DataRequired()])
    marks9 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt10 = StringField('Prompt', validators=[DataRequired()])
    answer10 = StringField('Answer', validators=[DataRequired()])
    marks10 = IntegerField('Marks', validators=[DataRequired()])
    
class OpenTestQuestion(FlaskForm):
    unitName = StringField('UnitName', validators=[DataRequired()])
    unitCode = StringField('UnitCode', validators=[DataRequired()])
    testNumber = IntegerField('TestName', validators=[DataRequired()])
    totalMarks = IntegerField('TotalMarks', validators=[DataRequired()])

    prompt1 = StringField('Prompt', validators=[DataRequired()])
    marks1 = IntegerField('Marks', validators=[DataRequired()])

    prompt2 = StringField('Prompt', validators=[DataRequired()])
    marks2 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt3 = StringField('Prompt', validators=[DataRequired()])
    marks3 = IntegerField('Marks', validators=[DataRequired()])

    prompt4 = StringField('Prompt', validators=[DataRequired()])
    marks4 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt5 = StringField('Prompt', validators=[DataRequired()])
    marks5 = IntegerField('Marks', validators=[DataRequired()])

    prompt6 = StringField('Prompt', validators=[DataRequired()])
    marks6 = IntegerField('Marks', validators=[DataRequired()])

    prompt7 = StringField('Prompt', validators=[DataRequired()])
    marks7 = IntegerField('Marks', validators=[DataRequired()])

    prompt8 = StringField('Prompt', validators=[DataRequired()])
    marks8 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt9 = StringField('Prompt', validators=[DataRequired()])
    marks9 = IntegerField('Marks', validators=[DataRequired()])
    
    prompt10 = StringField('Prompt', validators=[DataRequired()])
    marks10 = IntegerField('Marks', validators=[DataRequired()])
