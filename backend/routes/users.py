from flask import Blueprint, json, Response
from database.models import User
users_blueprint = Blueprint('users', __name__)


@users_blueprint.route('/')
def get_users():
    users = User.query.all()
    users_list = [user.to_dict() for user in users]
    return Response(json.dumps(users_list), status=200, content_type='application/json')
