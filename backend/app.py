
from flask import Flask, jsonify, request, Response, redirect
from flask_cors import CORS, cross_origin
from database.db import db
from database.models import User
from database.util import create_user
from dotenv import load_dotenv
from pysteamsignin.steamsignin import SteamSignIn
from database.util import create_user, find_user
import bcrypt
import requests
import os
import json

load_dotenv()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = os.urandom(24)


@app.route("/api/login-success")
def login_success():
    return Response(
        response=json.dumps({"status": "Login Success"}),
        status=201, mimetype="application/json")


@app.route("/api/login-failure")
def login_failure():
    return Response(
        response=json.dumps({"status": "Login Failure"}),
        status=401, mimetype="application/json")



@app.route("/")
def steam_login():
    apikey = request.values.get('apikey')
    login = SteamSignIn()
    return login.RedirectUser(login.ConstructURL(f"http://localhost:8000/api/login?apikey={apikey}"))


@app.route("/api/users")
def get_users():
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list)


@app.route("/api/login")
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

@app.route("/api/applogin", methods=['POST'])
def account_login():
    email = request.form['email']
    apikey_hash = str(bcrypt.hashpw(
        request.form['apikey'].encode('utf-8'), bcrypt.gensalt()))
    user = User.query.filter_by(email=email).first()

    # Database hash isnt the same as input hash. Could be bcrypt.gensalt()^^^
    # Fixed with encoding and decoding hash strings rather than using str()
    if bool(user):
        byte_hash = user.apikey
        print("Database: " + byte_hash + "\nUser: " + apikey_hash)
        if byte_hash == apikey_hash:
            return Response("Login Successful", status=200, mimetype='application/json')

    return Response("Login Failed", status=401, mimetype='application/json')


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

@app.route("/api/auth/register", methods=['POST'])
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
        player_summary = get_player_summary_manual(id)["response"]["players"][0]

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


def get_player_summary_manual(id):
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
      
   
@app.route("/api/getplayersummary", methods=['POST'])
def get_player_summary():
    url = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"
    print("HELP: " + request.form["apikey"])
    if "steamids" in request.form.keys():
        params = {
            "key": request.form["apikey"],
            "steamids": request.form["steamids"]
        }
        response = requests.get(url=url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return 'failure to get steam level games. Error: HTTP {}'.format(response.status_code)
    else:
        return "invalid steamid"

@app.route("/dev/test_db")
def test_create_user_1():
    user = {
        "steamid": str(os.urandom(17).hex()),
        "email": str(os.urandom(10).hex()) + "@gmail.com",
        "username": "Test_Case_1",
        "password": "wildcat",
        "logintype": "Steam",
        "apikey": str(os.urandom(24).hex()),
        "steamurl": "http://url.jpg",
        "fullavatarurl": "http://avatar.jpg"
    }

    result = create_user(user)
    return str(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
