# Main file for the Flask application

#   Importing required dependencies
from flask import Flask
from flask_cors import CORS
from flask_session import Session

#   Custom modules
from lib.config.config import DevelopmentConfig, ProdConfig
from lib.config.logger import AppWatcher
#   Initializing the Flask application
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
CORS(app, resources={r"/*": {"origins": "*"}})

Session(app)

log = AppWatcher()
@app.after_request
async def after_request(response):

    
    response.headers['clicks'] = 0
    response.headers['Expires'] = 0
    response.headers['Pragma'] = "no-cache"
    response.headers['Cache-Control'] = "no-cache, no-store, must-revalidate"
    
    #  Log the request
    log.log.info("Request has been made")
    
    return response

#   Endpoints

#   Log the application is running
log.log.info("App is running")

#   Run the application
if __name__ == '__main__':
    app.run()