# Main file for the Flask application

#   Importing required dependencies
from flask import Flask
from flask_cors import CORS
from flask_session import Session

#   Custom modules
from lib.config import DevelopmentConfig, ProdConfig

#   Initializing the Flask application
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
CORS(app, resources={r"/*": {"origins": "*"}})

Session(app)

@app.after_request
async def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

#   Endpoints

if __name__ == '__main__':
    app.run()