from main import app
from manager.json_response import response
import jinja2
my_loader = jinja2.ChoiceLoader([app.jinja_loader,jinja2.FileSystemLoader(['modules'])])
app.jinja_loader = my_loader

from users.router import users
app.register_blueprint(users)

@app.route('/')
def index():
    return "welcome to Meeber py V1.0"

@app.errorhandler(405)
def r405(e):
	return response(code=405,message=str(e))

@app.errorhandler(404)
def r404(e):
	return response(code=404,message=str(e))