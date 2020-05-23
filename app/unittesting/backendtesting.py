import unittest, os
from app import app, db
from app.models import User

class UserModelCase(unittest.TestCase):

  def setUp(self):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config(SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'test.db'))
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

  def test_password_hashing(self):
    setUp()
    s = User.query.get('111')
    s = User.set_password('hashpassword')
    self.assertFalse(s.check_password('secretpassword'))
    self.assertTrue(s.check_password('hashpassword'))
    tearDown()

if __name__ == '__main__':
  unittest.main()


  # def test_is_commited(self):
  #   s = User.query.get('111')
  #   self.assertFalse(s.is_commited())
  #   a = User.query.get('333')

