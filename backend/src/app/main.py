# import sys
# sys.path.insert(0, '../internal')
from pathlib import Path
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from internal import db
from query import steam_query
from controller import user
from flask import Flask, request, redirect, url_for, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

from app import account


USER = user.User("Dilian1")


@app.route("/profile", methods=['GET'])
def profile():
    return steam_query.get_profile(USER.get_steam_id(), USER.get_api_key())

@app.route("/owned-games", methods=['GET'])
def owned_games():
    return steam_query.get_owned_games(USER.get_steam_id(), USER.get_api_key())

@app.route("/get-app-image", methods=['POST'])
def app_image():
    request_data = request.get_json()
    appid = request_data['appid']
    return jsonify(url=steam_query.get_app_img_url(appid, USER.get_steam_id(), USER.get_api_key()))

@app.route("/get-steamid", methods=['GET'])
def get_steamid():
    return USER.get_steam_id()

@app.route("/appid-to-app-name", methods=['POST'])
def appid_to_appname():
    request_data = request.get_json()
    appid = request_data['appid']
    return steam_query.appid_to_name_converter(appid)

@app.route("/failure")
def createaccount_failure():
    return jsonify(success=0)

@app.route("/success")
def createaccount_success():
    return jsonify(success=1)


if __name__ == "__main__":
    app.run("localhost", port=5000, debug=True)