# Main file for the Flask application

#   Importing required dependencies
import os

from flask import Flask
from flask_cors import CORS
from flask_session import Session

from dotenv import load_dotenv

#   Load the environment variables
load_dotenv()

#   Custom modules
from lib.config.logger import AppWatcher
from lib.endpoints.cookies import Cookies
from lib.config.config import DevelopmentConfig, ProdConfig


#   Initialize the logger
logger = AppWatcher()
logger.FileHandler()

#   Initializing the Flask application
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

ALLOWED_ORIGIN = os.getenv('CORS_ORIGIN') if app.config['DEBUG'] == False else "*"
CORS(app, resources={r"/.*": {"origins": f"{ALLOWED_ORIGIN}"}})


Session(app)


@app.after_request
def after_request(response):

    response.headers['Expires'] = 0
    response.headers['Pragma'] = "cache"
    response.headers['Cache-Control'] = "no-cache, store, must-revalidate"
    
    #  Log the request
    return response

#   Endpoints
app.add_url_rule('/', view_func=Cookies().as_view('cookies', methods=['GET', 'POST']))

logger.info(f"App Configurations: {app.config}")
logger.info(f"ALLOWED ORIGINS: {ALLOWED_ORIGIN}")
logger.info("Application started")
#   Run the application
if __name__ == '__main__':
    app.run()