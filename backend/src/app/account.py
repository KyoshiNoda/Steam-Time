from pathlib import Path
import sys
path = str(Path(Path(__file__).parent.absolute()).parent.absolute())
sys.path.insert(0, path)

from internal import db
from controller import user
from flask import request, jsonify
from __main__ import app

@app.route("/create-account", methods=['POST'])
def create_account():

    request_data = request.get_json()

    email = request_data['email']
    steam_name = request_data['steam_name']
    password = request_data['password']
    api_key = request_data['api_key']

    if db.check_existing_account(email) == None:
        return "internal server error"
    elif db.check_existing_account(email) == True:
        return jsonify(success=False, description="Account already exists")
    else:
        USER = user.User(steam_name)
        db.create_account(email, steam_name, password, api_key)
        return jsonify(success=True, description="Account created")

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        request_data = request.get_json()

        email = request_data['email']
        password = request_data['password']

        if db.compare_passwords(email, password):
            return jsonify(success=True, description="Login Successful")
        else:
            return jsonify(success=False, description="Login Failed")
    return "success!"

@app.route("/change-password", methods=['POST'])
def change_password():
    """
    NOT TESTED YET
    """
    request_data = request.get_json()

    email = request_data['email']
    password = request_data['password']
    new_password = request_data['new_password']

    if db.compare_passwords(email, password) == True:
        db.change_password(email, new_password)
        return jsonify(success=True, description="Password changed")
    else:
        return jsonify(success=False, description="Password change failed")

