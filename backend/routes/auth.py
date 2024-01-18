from flask import Blueprint, json, Response, request
from database.util import create_user
from steam.api import get_steam_id, get_player_summary
import bcrypt
auth_blueprint = Blueprint('auth', __name__)


@auth_blueprint.route("/register", methods=['POST'])
def manual_register():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        api_key = data.get('apiKey')
        steam_url = data.get('steamURL')
        if not email or not password or not api_key or not steam_url:
            return Response(status=400, response=json.dumps({'error': 'Missing required fields'}))

        hashed_api_key = bcrypt.hashpw(
            api_key.encode('utf-8'), bcrypt.gensalt()).decode()
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt()).decode()

        id = get_steam_id(steam_url)
        player_summary = get_player_summary(id)["response"]["players"][0]

        if not id or not player_summary:
            return Response(status=400, response=json.dumps({"error": "Steam API failed!"}), content_type='application/json')

        user = {
            "steamid": id,
            "email": email,
            "username": player_summary["personaname"],
            "password": hashed_password,
            "logintype": "manual",
            "apikey": hashed_api_key,
            "steamurl": steam_url,
            "fullavatarurl": player_summary["avatarfull"]
        }
        if create_user(user):
            return Response(status=200, response=json.dumps({"message": "User created successfully"}), content_type='application/json')
        else:
            return Response(status=409, response=json.dumps({"error": "User already exists"}), content_type='application/json')

    except Exception as e:
        return Response(status=500, response=json.dumps({"error": "Internal server error", "details": str(e)}))
