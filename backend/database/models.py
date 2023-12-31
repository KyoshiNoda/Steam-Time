from database.db import db

class User(db.Model):
  __tablename__ = 'users'

  userid = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(255))
  firstname = db.Column(db.String(255))
  lastname = db.Column(db.String(255))
  password = db.Column(db.String(255))
  apikey = db.Column(db.String(255))

  def to_dict(self):
    return {
      'userid': self.userid,
      'email': self.email,
      'firstname': self.firstname,
      'lastname': self.lastname,
      'password': self.password,
      'apikey': self.apikey
    }