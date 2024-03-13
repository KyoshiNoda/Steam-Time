from database.db import db
from database.models import User
import bcrypt

def create_user(userdata: dict):
    user = User(
        steamid=userdata.get("steamid"),
        email=userdata.get("email"),
        username=userdata.get("username"),
        password=userdata.get("password"),
        logintype=userdata.get("logintype"),
        apikey=userdata.get("apikey"),
        steamurl=userdata.get("steamurl"),
        fullavatarurl=userdata.get("fullavatarurl")
    )
    try:
        db.session.add(user)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        return False
    
def update_user(email, userdata: dict):
    try:
        # with db.session.begin(subtransactions=True):
        user = User.query.filter_by(email=email).first()
        if user:
            for key, value in userdata.items():
                setattr(user, key, value)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(e)
        return False 

def find_user(steamid):
    user = User.query.filter_by(steamid=steamid).first()
    return bool(user)

def find_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return bool(user)

def verify_password(email, password):
    user = User.query.filter_by(email=email).first()
    return bcrypt.checkpw(password.encode(), user.password.encode())
    