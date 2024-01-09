from flask import Flask, jsonify, request, Response
from database.db import db
from database.models import User
from dotenv import load_dotenv
from pysteamsignin.steamsignin import SteamSignIn
import bcrypt
import requests
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
  
@app.route("/api/createaccount", methods=['POST'])
def create_account():
  userid=request.form['userid']
  email=request.form['email']
  firstname=request.form['firstname']
  lastname=request.form['lastname']
  apikey_hash = str(bcrypt.hashpw(request.form['apikey'].encode('utf-8'), bcrypt.gensalt()))
  
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
