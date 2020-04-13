from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
  # column_name = db.Column(variable_type, column_attribute_1, column_attribute_2, column_attribute_3, ...)
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(64), index = True, unique = True)
  email = db.Column(db.String(120), index = True, unique = True)
  password_hash = db.Column(db.String(128))
  admin = db.Column(db.Boolean, default=False)

  def __repr__(self): # How to print an instance of this class
    return '<User {}>'.format(self.username)

  # Password hashing functions: These are single-line functions encased in wrappers to access properties of the User self object
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)
  
  def toggle_admin(self):
    self.admin = not self.admin
  def check_admin(self):
    return self.admin

# Returns the User object associated with a particular input ID
# This function is called whenever a logged-in user navigates to another page on the microblog, and persists until the user is logged out.
@login.user_loader
def load_user(id):
  return User.query.get(int(id))