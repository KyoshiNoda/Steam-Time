import steam_query
import user

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
user1 = user.User("Dilian1")


@app.route("/profile", methods=['GET'])
def profile():
    return steam_query.get_profile(user1.get_steam_id(), user1.get_api_key())

@app.route("/ownedgames", methods=['GET'])
def owned_games():
    return steam_query.get_owned_games(user1.get_steam_id(), user1.get_api_key())

@app.route("/getappimage", methods=['POST', 'GET'])
def app_image():
    if request.method == 'POST':
        appid = request.form['appid']
    return steam_query.get_app_img_url(appid, user1.get_steam_id(), user1.get_api_key())

@app.route("/getsteamid", methods=['GET'])
def name_to_steamid():
    return user1.get_steam_id()

@app.route("/appidtoappname", methods=['POST', 'GET'])
def appid_to_appname():
    if request.method == 'POST':
        appid = request.form['appid']
        return steam_query.appid_to_name_converter(appid)


# @app.route("/login", method=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['name']



if __name__ == "__main__":
    app.run("localhost", 6969)