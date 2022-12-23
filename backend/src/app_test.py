from flask import Flask, request
app = Flask(__name__)
import steam_query_class

query_object = steam_query_class.Steam_WebAPI_Query("Dilian1")


@app.route("/profile", methods=['GET'])
def profile():
    return query_object.get_profile()

@app.route("/owned-games", methods=['GET'])
def owned_games():
    return query_object.get_owned_games()

@app.route("/get-app-image", method=['POST', 'GET'])
def app_image():
    if request.method == 'POST':
        appid = request.form['appid']
    return query_object.get_app_img_url(appid)

@app.route("/get_steamid", method=['GET'])
def name_to_steamid():
    return query_object.steam_id


# @app.route("/login", method=['POST', 'GET'])
# def login():
#     if request.method == 'POST':
#         user = request.form['name']



if __name__ == "__main__":
    app.run("localhost", 6969)