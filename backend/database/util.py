from database.db import db
from database.models import User


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
        return user.to_dict()
    except Exception as e:
        db.session.rollback()
        return None


def find_user(steamid):
    user = User.query.filter_by(steamid=steamid).first()
    return user.to_dict() if user else None


def update_user(steamid, new_fields):
    try:
        user = User.query.filter_by(steamid=steamid).first()
        if user:
            for key, value in new_fields.items():
                setattr(user, key, value)
            db.session.commit()
            return True
        else:
            return False
    except Exception as e:
        db.session.rollback()
        return False
