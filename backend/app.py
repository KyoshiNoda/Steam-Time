from flask import Flask, jsonify
from database.db import db
from database.models import User
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def base_url():
  return "<p>Hello World</p>"

@app.route("/api/users")
def get_users():
  users = User.query.all()
  users_list = [user.to_dict() for user in users]
  return jsonify(users_list)

if __name__ == '__main__':
  app.run(port=8000, debug=True)