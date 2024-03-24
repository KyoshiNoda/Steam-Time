from database.util import *
from flask import Blueprint, json, Response, request
from steam.api import *
import bcrypt
import jwt
auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route("/register", methods=['POST'])
def manual_register():
    try:
        request_data = request.json
        email = request_data.get('email')
        password = request_data.get('password')
        api_key = request_data.get('apiKey')
        steam_url = request_data.get('steamURL')
        if not email or not password or not api_key or not steam_url:
            return Response(status=400, response=json.dumps({'error': 'Missing required fields'}))

        steam_id = get_steam_id(steam_url, api_key)

        hashed_api_key = bcrypt.hashpw(
            api_key.encode('utf-8'), bcrypt.gensalt()).decode()
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt()).decode()

        response = get_player_summary(steam_id, api_key)[
            "response"]["players"][0]

        if not steam_id or not response:
            return Response(status=400, response=json.dumps({"error": "Steam API failed!"}), content_type='application/json')

        user = {
            "steam_id": steam_id,
            "email": email,
            "username": response["personaname"],
            "password": hashed_password,
            "login": "manual",
            "api_key": hashed_api_key,
            "steam_url": steam_url,
            "full_avatar_url": response["avatarfull"]
        }
        if create_user(user):
            payload = {'user_id': user['steam_id']}
            token = jwt.encode(payload, os.getenv('JWT_KEY'), algorithm='HS256').decode('utf-8')
            return Response(status=200, response=json.dumps({
                                                            "message": "User created successfully",
                                                            "user": user,
                                                            "token": token
                                                            }), content_type='application/json')
        else:
            return Response(status=409, response=json.dumps({"error": "User already exists"}), content_type='application/json')

    except Exception as e:
        return Response(status=500, response=json.dumps({"error": "Internal server error", "details": str(e)}))



@auth_blueprint.route("/login", methods=["POST"])
def manual_login():
    try:
        email = request.form['email']
        password = request.form['password']

        if find_user_by_email(email) and verify_password(email, password):
            return Response("Login Successful", status=200, mimetype='application/json')
        return Response("Login Failed", status=401, mimetype='application/json')

    except Exception as e:
        return Response(status=500, response=json.dumps({"error": "Internal server error", "details": str(e)}))
