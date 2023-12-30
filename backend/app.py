from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def base_url():
  return "<p>Hello World</p>"

@app.route("/api/users")
def get_users():
    data = {
       'firstName': 'Kyoshi',
       'lastName': 'Noda'
    }
    return jsonify(data)

app.run(port=8000, debug=True)