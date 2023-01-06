import steam_query
import hash
import db
import user
from flask import Flask, request, redirect, url_for
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


USER = user.User("test@example.com", "Dilian1")


@app.route("/profile", methods=['GET'])
def profile():
    return steam_query.get_profile(USER.get_steam_id(), USER.get_api_key())

@app.route("/ownedgames", methods=['GET'])
def owned_games():
    return steam_query.get_owned_games(USER.get_steam_id(), USER.get_api_key())

@app.route("/getappimage", methods=['POST', 'GET'])
def app_image():
    if request.method == 'POST':
        appid = request.form['appid']
    return steam_query.get_app_img_url(appid, USER.get_steam_id(), USER.get_api_key())

@app.route("/getsteamid", methods=['GET'])
def get_steamid():
    return USER.get_steam_id()

@app.route("/appidtoappname", methods=['POST', 'GET'])
def appid_to_appname():
    if request.method == 'POST':
        appid = request.form['appid']
        return steam_query.appid_to_name_converter(appid)

@app.route("/failure", methods=["GET"])
def createaccount_failure():
    return {"success": 0}

@app.route("/success", methods=["GET"])
def createaccount_success():
    return {"success": 1}

@app.route("/createaccount", methods=['POST', 'GET'])
def create_account():
    if request.method == 'POST':
        email = request.form['email']
        steam_name = request.form['steam_name']
        password = hash.hash_string(request.form['password'])
        api_key = hash.hash_string(request.form['api_key'])
        if db.get_account(email) != None:
            return redirect(url_for('/createaccount/failure'))
        else:
            USER = user.User(email, steam_name, api_key)
            return redirect(url_for('/createaccount/success'))
    return {"Create an account!"}

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if db.compare_passwords(email, password) == True:
            return redirect(url_for("/success"))
        else:
            return redirect(url_for("/failure"))

@app.route("/change-password", methods=['POST', 'GET'])
def change_password():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        new_password = request.form['new_password']

        if db.compare_passwords(email, password) == True:
            db.change_password(email, new_password)
            return redirect(url_for("/success"))
        else:
            return redirect(url_for("/failure"))


if __name__ == "__main__":
    app.run("localhost", 6969)