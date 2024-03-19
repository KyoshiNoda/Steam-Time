from flask import Blueprint, json, Response, request
from database.models import User
from database.util import update_user
import bcrypt
users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/')
def get_users():
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return Response(json.dumps(users_list), status=200, content_type='application/json')

@users_blueprint.route("change-information", methods=["PATCH"])
def change_user_information():
    changes = {
        "email": request.form['email'],
        "apikey": bcrypt.hashpw(
            request.form['apikey'].encode('utf-8'), bcrypt.gensalt()).decode(),
        "steamurl": request.form['steamurl']
    }

    if update_user(request.form['email'], changes):
        return Response(status=200, response=json.dumps({"message": "User information changed successfully"}), content_type='application/json')
    else:
        return Response(status=400, response=json.dumps({"error": "User information not changed"}), content_type='application/json')
    
@users_blueprint.route("change-password", methods=["PATCH"])
def change_user_password():
    changes = {
        "password": bcrypt.hashpw(
            request.form['password'].encode('utf-8'), bcrypt.gensalt()).decode()
    }

    if update_user(request.form['email'], changes):
        return Response(status=200, response=json.dumps({"message": "User password changed successfully"}), content_type='application/json')
    else:
        return Response(status=400, response=json.dumps({"error": "User password not changed"}), content_type='application/json')





