from flask import Flask
app = Flask(__name__)
import steam_query_class

query_object = steam_query_class.Steam_WebAPI_Query(76561198871279330)


@app.route("/profile", methods=['GET'])
def profile():
    return query_object.get_profile()

@app.route("/ownedgames", methods=['GET'])
def ownedgames():
    return query_object.get_owned_games()


if __name__ == "__main__":
    app.run("localhost", 6969)