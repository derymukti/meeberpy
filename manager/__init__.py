from flask_script import Manager, Command, Server
from main import app,db,running
from models import *
managers = Manager(app, usage="Meeber Python V1.0", with_default_commands=False)
managers.add_command('run', running)
@managers.command
def migrate():
    """ To migrate model"""
    try:
        db.create_all()
        print "Migrate success"
    except Exception as err:
		exit(err)

@managers.command
def seed():
    """ To seed data"""
    try:
        return seed_data()
    except Exception as err:
		exit(str(err))
