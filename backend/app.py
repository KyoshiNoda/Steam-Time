from flask import Flask, jsonify, request
from database.db import db
from database.models import User
from dotenv import load_dotenv
from pysteamsignin.steamsignin import SteamSignIn
import requests
import bcrypt
import os
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.route("/")
def steam_login():
    login = SteamSignIn()
    return login.RedirectUser(login.ConstructURL('http://localhost:8000/api/login'))


# @app.route("/api/users")
# def get_users():
#     users = User.query.all()
#     users_list = [user.to_dict() for user in users]
#     return jsonify(users_list)


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

        if not email or not password or not api_key:
            return jsonify({'error': 'Missing required fields'}), 400

        hashed_api_key = bcrypt.hashpw(
            api_key.encode('utf-8'), bcrypt.gensalt()).decode()

        response = get_player_summary(api_key, api_key)
        if response.status_code == 200:
            return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# response = get_player_summary()
# if response.status_code == 200:
#     # make a user
#     user.name = response.response.players[0].personaname
#     user.steamurl = response.response.players[0].profileurl
#     user.fullavatarurl = response.response.players[0].avatarfull


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


def get_player_summary(apikey, steamids):
    url = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002"
    params = {
        "key": apikey,
        "steamids": steamids
    }
    response = requests.get(url=url, params=params)
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return 'Failure to get steam level games. Error: HTTP {}'.format(response.status_code), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
