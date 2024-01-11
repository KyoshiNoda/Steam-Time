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
        return True
    except Exception as e:
        db.session.rollback()
        return False