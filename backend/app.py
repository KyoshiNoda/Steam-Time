from flask import Flask, jsonify, request, Response
from database.db import db
from database.models import User
from database.util import create_user
from dotenv import load_dotenv
from pysteamsignin.steamsignin import SteamSignIn
import requests
import bcrypt
import os
import json

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def steam_login():
    login = SteamSignIn()
    return login.RedirectUser(login.ConstructURL('http://localhost:8000/api/login'))


@app.route("/api/users")
def get_users():
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list)


@app.route("/api/login")
def login_process():
    data = request.values
    login = SteamSignIn()
    steam_id = login.ValidateResults(data)
    if steam_id:
        return jsonify({'steam_id': '{}'.format(steam_id)})
    else:
        return 'failed login.'


@app.route("/api/auth/register", methods=['POST'])
def manual_register():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        api_key = data.get('apikey')
        steam_url = data.get('steamurl')
        if not email or not password or not api_key or not steam_url:
            return Response(status=400, response=json.dumps({'error': 'Missing required fields'}))

        hashed_api_key = bcrypt.hashpw(
            api_key.encode('utf-8'), bcrypt.gensalt()).decode()

        id = get_steam_id(steam_url)
        player_summary = get_player_summary(id)["response"]["players"][0]

        if not id or not player_summary:
            return Response(status=400, response=json.dumps({"error": "Steam API failed!"}), content_type='application/json')

        user = {
            "steamid": id,
            "email": email,
            "username": player_summary["personaname"],
            "password": hashed_api_key,
            "logintype": "manual",
            "apikey": os.getenv('API_KEY'),
            "steamurl": steam_url,
            "fullavatarurl": player_summary["avatarfull"]
        }
        if create_user(user):
            return Response(status=200, response=json.dumps({"message": "User created successfully"}), content_type='application/json')
        else:
            return Response(status=409, response=json.dumps({"error": "User already exists"}), content_type='application/json')

    except Exception as e:
        return Response(status=500, response=json.dumps({"error": "Internal server error", "details": str(e)}))


def get_steam_id(url):
    if "/id/" in url:
        parts = url.split("/id/")
        if len(parts) >= 2:
            steamid_response = get_steam_id_api(parts[1][:-1])["response"]
            if steamid_response["success"] == 1:
                return steamid_response["steamid"]
            else:
                return parts[1][:-1]
    else:
        return None


def get_steam_id_api(url):
    steam_api_url = "http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/"
    params = {
        "key": os.getenv('API_KEY'),
        "vanityurl": url
    }
    response = requests.get(url=steam_api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return 'Failure to get steam id. Error: HTTP {}, {}'.format(response.status_code)


def get_player_summary(id):
    steam_api_url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    params = {
        "key": os.getenv("API_KEY"),
        "steamids": id,
        "format": "json"
    }
    response = requests.get(url=steam_api_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return 'Failure to get steam id. Error: HTTP {}, {}'.format(response.status_code)


@app.route("/api/ownedgames")
def get_owned_games():
    url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/"
    data = request.values
    if "steamid" in data.keys():
        params = {
            "key": os.getenv('API_KEY'),
            "steamid": data['steamid']
        }
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return 'failure to get owned games. Error: HTTP {}'.format(response.status_code)
    else:
        return 'invalid steamid'


@app.route("/api/recentlyplayedgames")
def get_recently_played_games():
    url = "https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1"
    data = request.values
    if "steamid" in data.keys():
        params = {
            "key": os.getenv('API_KEY'),
            "steamid": data['steamid']
        }
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return 'failure to get recently played games. Error: HTTP {}'.format(response.status_code)
    else:
        return "invalid steamid"


@app.route("/api/steamlevel")
def get_steam_level():
    url = "https://api.steampowered.com/IPlayerService/GetSteamLevel/v1"
    data = request.values
    if "steamid" in data.keys():
        params = {
            "key": os.getenv('API_KEY'),
            "steamid": data['steamid']
        }
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return 'failure to get steam level games. Error: HTTP {}'.format(response.status_code)
    else:
        return "invalid steamid"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
