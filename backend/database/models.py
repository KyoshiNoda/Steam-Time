from database.db import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    steam_id = db.Column(db.String(17))
    email = db.Column(db.String(255))
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    login = db.Column(db.String(255))
    api_key = db.Column(db.String(255))
    steam_url = db.Column(db.String(255))
    full_avatar_url = db.Column(db.String(255))

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'steam_id': self.steam_id,
            'email': self.email,
            'username': self.username,
            'password': self.password,
            'login': self.login,
            'api_key': self.api_key,
            'steam_url': self.steam_url,
            'full_avatar_url': self.full_avatar_url
        }
