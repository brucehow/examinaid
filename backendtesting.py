import unittest, os
from app import app, db
##from config import Config
from app.models import User
from app.forms import ResetPasswordForm, LoginForm, RegisterForm, TestForm, MultiTestQuestion, ShortTestQuestion, OpenTestQuestion
from wtforms.validators import ValidationError, Email, EqualTo
class UserModelCase(unittest.TestCase):

  def setUp(self):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'test.db')
    
    self.app = app.test_client() #creates virtual test enviroment
    db.create_all()
    s1 = User(id = 111, username="testing101", email="tester@gmail.com", password_hash = "secretpassword", admin = False)
    s2 = User(id = 222, username="testing202", email="tester2@gmail.com", password_hash = "secretpassword2")
    a1 = User(id = 333, username="admin101", email="admin@gmail.com", password_hash = "adminiscool", admin = True)
    a2 = User(id = 4444, username="admin404", email="admin4@gmail.com", password_hash = "adminiscool4", admin = True)
    db.session.add(s1)
    db.session.add(s2)
    db.session.add(a1)
    db.session.add(a2)
    db.session.commit()
  
  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_user_username(self):
    user1 = User.query.get('111')
    self.assertEqual(user1.username, "testing101")

  def test_admin_username(self):
    admin1 = User.query.get('333')
    self.assertEqual(admin1.username, "admin101")

  def test_user_email(self):
    user1 = User.query.get('111')
    self.assertEqual(user1.email, "tester@gmail.com")

  def admin_user_email(self):
    admin1 = User.query.get('333')
    self.assertEqual(admin1.email, "admin@gmail.com")

  def check_password(self):
    s = User.query.get('111')
    a = User.query.get('333')
    self.assertEqual(s.check_password, 'secretpassword')
    self.assertEqual(a.check_password, 'adminiscool')


  def test_set_password(self):
    s = User.query.get('111')
    a = User.query.get('333')
    s.set_password('hashpassword')
    a.set_password('newpassword')
    self.assertFalse(s.check_password('secretpassword'))
    self.assertTrue(s.check_password('hashpassword'))
    self.assertFalse(a.check_password('adminiscool'))
    self.assertTrue(a.check_password('newpassword'))

  def test_password_hashing(self):
    s = User.query.get('111')
    s.set_password('hashedpassword')
    self.assertNotEqual(s.password_hash, 'hashedpassword')

  def test_check_admin(self):
    s = User.query.get('111')
    a = User.query.get('333')
    self.assertFalse(s.check_admin())
    self.assertTrue(a.check_admin())   

  def test_toggle_admin(self):
    s = User.query.get('111')
    a = User.query.get('333')
    s.toggle_admin()
    a.toggle_admin()
    self.assertTrue(s.check_admin())
    self.assertFalse(a.check_admin())

  # def test_validate_email(self):
  #   s = User.query.get('111')
  #   with self.assertRaises(ValidationError):
  #     ResetPasswordForm.validate_email(s.email, 'tester2@gmail.com')

if __name__ == '__main__':
  unittest.main(verbosity=2)


