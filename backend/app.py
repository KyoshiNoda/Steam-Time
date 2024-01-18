import os
from flask import Flask
from flask_cors import CORS
from database.db import db
from dotenv import load_dotenv
from routes.users import users_blueprint
from routes.auth import auth_blueprint
from routes.steam_auth import steam_auth_blueprint

load_dotenv()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = os.urandom(24)

app.register_blueprint(users_blueprint, url_prefix='/api/users')
app.register_blueprint(auth_blueprint, url_prefix='/api/auth')
app.register_blueprint(steam_auth_blueprint, url_prefix='/api/steamAuth')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
