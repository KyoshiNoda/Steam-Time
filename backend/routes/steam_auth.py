import bcrypt
import requests
import json
from flask import redirect, request, Response, Blueprint
from pysteamsignin.steamsignin import SteamSignIn
from database.util import create_user, find_user

steam_auth_blueprint = Blueprint('steam_auth', __name__)


@steam_auth_blueprint.route("/")
def steam_login():
    apikey = request.values.get('apikey')
    login = SteamSignIn()
    return login.RedirectUser(login.ConstructURL(f"http://localhost:8000/api/login?apikey={apikey}"))


@steam_auth_blueprint.route("/login")
def login_process():
    data = request.values
    login = SteamSignIn()
    steamid = login.ValidateResults(data)
    apikey = data.get("apikey")
    response = requests.post(
        url="http://localhost:8000/api/getplayersummary",
        data={
            "steamids": steamid,
            "apikey": apikey
        }).json()['response']['players'][0]

    apikey = (bcrypt.hashpw(apikey.encode('utf-8'), bcrypt.gensalt())).decode()
    print("HERE" + str(find_user(steamid)))
    if find_user(steamid):
        return redirect("http://localhost:8000/api/login-success")
    else:
        print("login bc no entry")
        db_resp = create_user(
            {
                "steamid": steamid,
                "username": response['personaname'],
                "logintype": "Steam",
                "apikey": apikey,
                "steamurl": response['profileurl'],
                "fullavatarurl": response["avatarfull"]
            })

        if db_resp == True:
            return redirect("http://localhost:8000/api/login-success")
        else:
            return redirect("http://localhost:8000/api/login-failure")




@steam_auth_blueprint.route("/login-success")
def login_success():
    return Response(
        response=json.dumps({"status": "Login Success"}),
        status=201, mimetype="application/json")


@steam_auth_blueprint.route("/login-failure")
def login_failure():
    return Response(
        response=json.dumps({"status": "Login Failure"}),
        status=401, mimetype="application/json")
