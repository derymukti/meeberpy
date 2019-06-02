from flask_script import Manager, Command, Option
import sys, os
from termcolor import colored

class Create(Command):
	
	help_args = ('-h', '--help')
	help = "Create Controller"
	option_list = (
        Option('--name', '-n', dest='name'),
    )
	def create_folder(self,name):
		directory = 'controllers/'+name
		if not os.path.exists(directory):
			os.makedirs(directory)
		if not os.path.exists(directory+'/modules'):
			os.makedirs(directory+'/modules')
		try:
			with open(directory+'/__init__.py','w') as f:
				f.write('import router')
				f.close()
		except Exception as err:
			exit(str(err))

		print "Meeberpy ==> "+directory+" ::::>> Created"
		print "Meeberpy ==> ", colored("controllers/"+name+"/modules/__init__.py","red")
		print colored("		edit this model file for modules file","red")
		print "Meeberpy ==> ", colored("controllers/"+name+"/router.py","red")
		print colored("		edit this router file for add new endpoint","red")
		print "Meeberpy ==> read github.com/derymukti/meeberpy"
		return directory

	def create_modules(self,name):
		try:
			with open('controllers/'+name+'/modules/__init__.py', 'w') as f:
				f.write("from flask import request,Response \n")
				f.write("from manager.json_response import response \n")
				f.write("def hello():\n")
				f.write('	return response(code=200,message="hello in %s controller")' % (name))
				f.close()
		except Exception as err:
			exit(str(err))
 
	def create_router(self,name):
		try:
			with open('controllers/'+name+'/__init__.py', 'w') as f:
				f.write("import router")
				f.close()
			with open('controllers/'+name+'/router.py', 'w') as f:
				f.write("from flask import Blueprint, request\n")
				f.write("from modules import *\n")
				f.write("%s = Blueprint('%s', __name__, url_prefix='/%s')\n\n" % (name,name,name))
				f.write("@%s.route('/')\n" % (name))
				f.write("def index():\n")
				f.write("	return hello()\n")
				f.close()
		except Exception as err:
			exit(str(err))

	def add_to_route(self,name):
		try:
			with open('controllers/__init__.py','r') as f:
				f.seek(0)
				data = f.readlines()
				a = len(data) - 1
				f.close()
				register_controller= "from "+name+".router import "+name+"\napp.register_blueprint("+name+")\n"
				d = open('controllers/__init__.py','w')
				data.insert(10,register_controller)
				d.writelines(data)
				d.close()
		except Exception as err:
			exit(str(err))

	def create_controller(self,name):
		self.create_folder(name)
		self.create_modules(name)
		self.create_router(name)
		self.add_to_route(name)

	def run(self, name):
		self.create_controller(name)