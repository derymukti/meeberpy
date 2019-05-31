from flask import Blueprint, request
from modules import *
users = Blueprint('users', __name__, url_prefix='/users')
@users.route('/')
def index():
    return hello()

@users.route('/data')
def get_data():
    return get()

@users.route('/data',methods=['POST'])
def store():
    return stores()

@users.route('/data',methods=['PUT'])
def update():
    return updates()

@users.route('/data',methods=['DELETE'])
def delete():
    return deletes()