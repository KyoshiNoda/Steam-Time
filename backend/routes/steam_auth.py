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
    api_key = request.values.get('api_key')
    login = SteamSignIn()
    return login.RedirectUser(login.ConstructURL(f"http://localhost:8000/api/steam_auth/steam-login?api_key={api_key}"))


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


@steam_auth_blueprint.route('/steam-api-key')
def api_key_check():
    try:
        data = request.values
        api_key = data.get("api_key")
        steam_id = data.get("steam_id")
        user = find_user(steam_id)

        if not user.api_key:
            update_user(steamid=user.steamid, new_fields={"api_key": api_key})
        else:
            response = get_player_summary(steam_id, api_key)
            if response == 200:
                data = response['response']['players'][0]
                # fix this below
                user = update_user(steamid=user.steam_id, new_fields={data})
                return Response(status=200, response=json.dumps({"message": "Updated User!", "updatedUser": user}), mimetype="application/json")
            else:
                return Response(status=400, response=json.dumps({"message": "Bad API Key"}))

    except Exception as e:
        return Response(status=500, response=json.dumps({"error": "Internal server error", "details": str(e)}))

    # print(response)
    # response = requests.post(
    #     url="http://localhost:8000/api/steamgetplayersummary",
    #     data={
    #         "steamids": steamid,
    #         "apikey": apikey
    #     }).json()['response']['players'][0]

    # api_key = (bcrypt.hashpw(api_key.encode(
    #     'utf-8'), bcrypt.gensalt())).decode()
    # if find_user(steam_id):
    #     return redirect("http://localhost:8000/api/login-success")
    # else:
    #     print("login bc no entry")
    #     db_resp = create_user(
    #         {
    #             "steamid": steam_id,
    #             "username": response['personaname'],
    #             "logintype": "Steam",
    #             "api_key": api_key,
    #             "steamurl": response['profileurl'],
    #             "fullavatarurl": response["avatarfull"]
    #         })
    #     if db_resp == True:
    #         return redirect("http://localhost:8000/api/login-success")
    #     else:
    #         return redirect("http://localhost:8000/api/login-failure")
