from flask import Flask, jsonify, request, Response, session
from database.db import db
from database.models import User
from dotenv import load_dotenv
from pysteamsignin.steamsignin import SteamSignIn
import bcrypt
import requests
import os
from database.util import create_user
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = os.urandom(24)

    
@app.route("/api/login-success")
def login_success():
    """
      user = User(db.find(steamid))
      if not user:
        response = api.getPlayerSummary(apiKey,steamId)
        user.name = response.name
        user.picture = response.picture....

        db.add_row(user)

      public_user = publicUser(user)
      return Response(201, public_user)
    """

    return Response(
        response=jsonify({"status": "Login Success"},
                         status=201, mimetype="application/json")
    )


@app.route("/api/login-failure")
def login_failure():
    return Response(
        response=jsonify({"status": "Login Failure"},
                         status=401, mimetype="application/json")
    )


@app.route("/")
def steam_login():
    apikey = request.values.get('apikey')
    login = SteamSignIn()
    return login.RedirectUser(login.ConstructURL(f"http://localhost:8000/api/login?api_key={apikey}"))

@app.route("/api/users")
def get_users():
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return jsonify(users_list)

@app.route("/api/login")
def login_process():
    data = request.values
    print("TEST: " + str(data))
    login = SteamSignIn()
    steam_id = login.ValidateResults(data)



""" 
  def sucess_login()j:
    if user:
      Response(200, user.json())
    else:
      db.add(user)
      Response(200,user.json())
    
"""


@app.route("/api/createaccount", methods=['POST'])
def create_account():
    userid = request.form['userid']
    email = request.form['email']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    apikey_hash = str(bcrypt.hashpw(
        request.form['apikey'].encode('utf-8'), bcrypt.gensalt()))

    if User.query.get(userid):
        return 'account already exists'
    elif bool(User.query.filter_by(email=email).first()):
        return 'email is in use'
    else:
        user = User(
            userid=userid,
            email=email,
            firstname=firstname,
            lastname=lastname,
            password='',
            apikey=apikey_hash
        )

        db.session.add(user)
        db.session.commit()
        return Response("Account Creation Successful", status=200, mimetype='application/json')


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
