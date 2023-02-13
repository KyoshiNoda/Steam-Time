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
    #return jsonify(app_name=steam_query.appid_to_name_converter(appid))

@app.route("/failure")
def createaccount_failure():
    return jsonify(success=0)

@app.route("/success")
def createaccount_success():
    return jsonify(success=1)

# @app.route("/create-account", methods=['POST'])
# def create_account():

#     request_data = request.get_json()

#     email = request_data['email']
#     steam_name = request_data['steam_name']
#     password = request_data['password']
#     api_key = request_data['api_key']

#     if db.check_existing_account(email) == None:
#         return "internal server error"
#     elif db.check_existing_account(email) == True:
#         # return redirect(url_for('/createaccount/failure'))
#         return jsonify(success=False, description="Account already exists")
#     else:
#         USER = user.User(steam_name)
#         # return redirect(url_for('/createaccount/success'))
#         db.create_account(email, steam_name, password, api_key)
#         return jsonify(success=True, description="Account created")

# @app.route("/login", methods=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         request_data = request.get_json()

#         email = request_data['email']
#         password = request_data['password']

#         if db.compare_passwords(email, password):
#             return jsonify(success=True, description="Login Successful")
#         else:
#             return jsonify(success=False, description="Login Failed")
#     return "success!"

# @app.route("/change-password", methods=['POST'])
# def change_password():
#     """
#     NOT TESTED YET
#     """
#     request_data = request.get_json()

#     email = request_data['email']
#     password = request_data['password']
#     new_password = request_data['new_password']

#     if db.compare_passwords(email, password) == True:
#         db.change_password(email, new_password)
#         return jsonify(success=True, description="Password changed")
#     else:
#         return jsonify(success=False, description="Password change failed")


if __name__ == "__main__":
    app.run("localhost", port=5000, debug=True)