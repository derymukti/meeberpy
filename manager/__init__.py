from flask_script import Manager, Command, Server
from main import app,db,debug,port,host,worker,threads
from models import *
from manager.create_controller import Create
import multiprocessing
import gunicorn.app.base
from gunicorn.six import iteritems
import logging

running = Server(host=host,port=int(port),use_debugger=debug,use_reloader=True,threaded=True)
managers = Manager(app, usage="Meeber Python V1.0", with_default_commands=False)
managers.add_command('run', running)
managers.add_command('create:controller',Create)

@managers.command
def migrate():
    """ To migrate model"""
    try:
        db.create_all()
        print "Migrate success"
    except Exception as err:
		exit(str(err))

@managers.command
def seed():
    """ To seed data"""
    try:
        return seed_data()
    except Exception as err:
		exit(str(err))

@managers.command
def start_gunicorn():
  """ Running with gunicorn server """
  class StandaloneApplication(gunicorn.app.base.BaseApplication):
      
      def __init__(self, app, options=None):
          self.options = options or {}
          self.application = app
          super(StandaloneApplication, self).__init__()

      def load_config(self):
          config = dict([(key, value) for key, value in iteritems(self.options)
                        if key in self.cfg.settings and value is not None])
          for key, value in iteritems(config):
              self.cfg.set(key.lower(), value)

      def load(self):
          return self.application
  
  options = {
        'bind': '%s:%s' % (host, port),
        'workers': number_of_workers(),
        'loglevel':'debug',
        'reload':True,
        'access_log_format':'%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"',
        'accesslog':'logs',
        'threads':int(threads),
    }
  StandaloneApplication(app, options).run()

def number_of_workers():
    if worker =='auto':
      return (multiprocessing.cpu_count() * 2) + 1
    else:
      return worker