import os
from flask import Flask, render_template

# Customize default templates and static folder paths.
static_folder_path = os.getcwd() + "/app/views/static/"
templates_folder_path = os.getcwd() + "/app/views/templates/"

# Initialize the application with modified configurations.
application = Flask(__name__, 
					template_folder = templates_folder_path, 
					static_folder = static_folder_path, 
					static_url_path='/assets')

# Load application configurations.
application.config.from_object('app.config')
application.debug = True

# Initialize the application controllers, models and business logic services.
from app.controllers import *
from app.models import *
from app.services import *

# Render not found page.
@application.errorhandler(404)
def page_not_found(e):
    return render_template('/errors/404.html')