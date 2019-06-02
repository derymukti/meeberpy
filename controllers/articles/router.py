from flask import Blueprint, request
from .modules import *
articles = Blueprint('articles', __name__, url_prefix='/articles')
@articles.route('/')
def index():
    return hello()

@articles.route('/data')
def get_data():
    return get()

@articles.route('/data',methods=['POST'])
def store():
    return stores()

@articles.route('/data',methods=['PUT'])
def update():
    return updates()

@articles.route('/data',methods=['DELETE'])
def delete():
    return deletes()