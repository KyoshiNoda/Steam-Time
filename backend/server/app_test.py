from flask import Flask
app = Flask(__name__)
import steam_query_class

@app.route("/profile", methods=['GET'])
def profile():
    query_object = steam_query_class.Steam_WebAPI_Query(76561198871279330)
    return query_object.get_profile()


if __name__ == "__main__":
    app.run("localhost", 6969)