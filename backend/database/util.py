from database.db import db
from database.models import User
import bcrypt

def create_user(userdata: dict):
    user = User(
        steam_id=userdata.get("steam_id"),
        email=userdata.get("email"),
        username=userdata.get("username"),
        password=userdata.get("password"),
        login=userdata.get("login"),
        api_key=userdata.get("api_key"),
        steam_url=userdata.get("steam_url"),
        full_avatar_url=userdata.get("full_avatar_url")
    )
    try:
        db.session.add(user)
        db.session.commit()
        return user.to_dict()
    except Exception as e:
        db.session.rollback()
        print(e)
        return e
    
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
    