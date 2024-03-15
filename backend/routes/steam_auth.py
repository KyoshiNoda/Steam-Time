from flask import redirect
import bcrypt
import json
from steam.api import *
from flask import redirect, request, Response, Blueprint
from pysteamsignin.steamsignin import SteamSignIn
from database.util import *
from database.models import User

steam_auth_blueprint = Blueprint('steam_auth', __name__)


@steam_auth_blueprint.route("/")
def steam_login():
    login = SteamSignIn()
    return login.RedirectUser(login.ConstructURL(f"http://localhost:8000/api/steam_auth/steam-login"))


@steam_auth_blueprint.route("/steam-login")
def login_process():
    try:
        data = request.values
        login = SteamSignIn()
        steam_id = login.ValidateResults(data)

        if steam_id:
            user = find_user(steam_id)
            if not user:
                new_user = {
                    "steam_id": steam_id,
                    "login": "steam",
                }
                created_user = create_user(new_user)
                response = redirect('http://localhost:3000/auth/main')
                response.headers[
                    'Location'] += f'?message=Login%20Success&user={json.dumps(created_user)}'
                return response
            else:
                response = redirect('http://localhost:3000/auth/main')
                response.headers[
                    'Location'] += f'?message=Login%20Success&user={json.dumps(user)}'
                return response
        else:
            return Response(
                response=json.dumps({"message": "Login Failed"}),
                status=400, mimetype="application/json"
            )

    except Exception as e:
        return Response(status=500, response=json.dumps({"error": "Internal server error", "details": str(e)}))


@steam_auth_blueprint.route('/new-user', methods=['POST'])
def api_key_check():
    try:
        request_data = request.json
        api_key = request_data.get('api_key')
        steam_id = request_data.get('steam_id')

        if not steam_id or not api_key:
            return Response(status=404, response=json.dumps({"error": "API KEY missing!"}))

        hashed_api_key = bcrypt.hashpw(
            api_key.encode('utf-8'), bcrypt.gensalt()).decode()

        user = update_user(steam_id, {"api_key": hashed_api_key})
        response = get_player_summary(steam_id, api_key)
        if response:
            data = response['response']['players'][0]
            user['steam_url'] = data['profileurl']
            user['full_avatar_url'] = data['avatarfull']
            user['username'] = data['personaname']
            updated_user = update_user(steam_id, user)
            return Response(status=200, response=json.dumps({"message": "Updated User!", "updatedUser": updated_user}), mimetype="application/json")
        else:
            return Response(status=400, response=json.dumps({"message": "Bad API Key"}))

    except Exception as e:
        return Response(status=500, response=json.dumps({"error": "Internal server error", "details": str(e)}))
