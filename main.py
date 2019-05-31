from flask import Flask
from flask_script import Server
import sys , json, MySQLdb, redis
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
import psycopg2

try:
	with open('config.json') as data:
		data_json = json.loads(data.read())
		db_host = data_json['db']['db_host']
		db_user = data_json['db']['db_user']
		db_pass = data_json['db']['db_pass']
		db_name = data_json['db']['db_name']
		host = data_json['host']
		port = data_json['port']
		debug = data_json['debug']
		secret = data_json['secret']
		
except Exception as err:
	exit(err)

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@%s:5432/%s' % (db_user,db_pass,db_host,db_name)
try:
	db = SQLAlchemy(app)
except Exception as err:
	exit(err)

import controllers

running = Server(host=host,port=int(port),use_debugger=debug,use_reloader=True,threaded=True)
import manager
import models
if __name__ == '__main__':
	manager.managers.run()