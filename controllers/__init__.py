from main import app
from manager.json_response import response
import jinja2,os
my_loader = jinja2.ChoiceLoader([app.jinja_loader,jinja2.FileSystemLoader(['modules'])])
app.jinja_loader = my_loader

from .articles.router import articles
app.register_blueprint(articles)

@app.route('/')
def index():
    return "welcome to Meeber py V1.0, response from %s \n" % (os.getpid())

@app.errorhandler(405)
def r405(e):
	return response(code=405,message=str(e))

@app.errorhandler(404)
def r404(e):
	return response(code=404,message=str(e))