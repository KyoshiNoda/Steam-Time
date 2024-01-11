from database.db import db


class User(db.Model):
    __tablename__ = 'users'

    userid = db.Column(db.Integer, primary_key=True)
    steamid = db.Column(db.String(17))
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    logintype = db.Column(db.String(255))
    apikey = db.Column(db.String(255))
    steamurl = db.Column(db.String(255))
    fullavatarurl = db.Column(db.String(255))

    def to_dict(self):
        return {
            'userid': self.userid,
            'steamid': self.steamid,
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'logintype': self.logintype,
            'apikey': self.apikey,
            'steamurl': self.steamurl,
            'fullavatarurl': self.fullavatarurl
        }
