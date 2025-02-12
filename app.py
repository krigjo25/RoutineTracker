# Main file for the Flask application

#   Importing required dependencies
from flask import Flask
from flask_cors import CORS
from flask_session import Session

#   Custom modules
from lib.config.logger import AppWatcher
from lib.endpoints.cookies import Cookies
from lib.config.config import DevelopmentConfig, ProdConfig

#   Initializing the Flask application
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
CORS(app, resources={r"/*": {"origins": "*"}})

Session(app)

log = AppWatcher()

@app.after_request
def after_request(response):


    response.headers['Expires'] = 0
    response.headers['Pragma'] = "cache"
    response.headers['Cache-Control'] = "no-cache, store, must-revalidate"
    
    #  Log the request
    return response

#   Endpoints
app.add_url_rule('/', view_func=Cookies().as_view(name ='index.html'))

#   Log the application is running
log.log.info("App is running")

#   Run the application
if __name__ == '__main__':
    app.run()