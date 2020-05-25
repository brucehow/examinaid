import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # os.environ returns a map containing the user's environmental variables
    # While the environmental variable 'SECRET_KEY' has not been set, the variable will attempt to look for it, and if it fails, will default to the second value.
    # The secret key is a builtin configuration value in Flask. See here: https://flask.palletsprojects.com/en/1.1.x/config/
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
