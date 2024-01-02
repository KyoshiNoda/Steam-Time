from flask import Flask, jsonify, request
from database.db import db
from database.models import User
from dotenv import load_dotenv
from pysteamsignin.steamsignin import SteamSignIn
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


if __name__ == '__main__':
  app.run(port=8000, debug=True)