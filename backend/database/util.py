from database.db import db
from database.models import User


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
        return None


def find_user(steam_id):
    user = User.query.filter_by(steam_id=steam_id).first()
    return user.to_dict() if user else None


def update_user(steam_id, new_fields):
    try:
        user = User.query.filter_by(steam_id=steam_id).first()
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
