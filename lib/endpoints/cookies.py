#   Flask Cookies
from flask.views import MethodView
from lib.config.logger import CookieWatcher
from flask import request, jsonify, make_response

#   Initialize the logger
logger = CookieWatcher()
logger.FileHandler()

class Cookies(MethodView):

    def __init__(self, *args, **kwargs):
        self.logger = logger
        self.cookie_name = "Click"

    def get(self):

        response = {}
        response['status'] = 200
        if request.cookies.get(self.cookie_name):

            response[self.cookie_name] = int(request.cookies.get(self.cookie_name))

            self.logger.info(f"Server response: {response}")

            return jsonify(response)

        else:
            self.logger.warn(f"Cookies not found, Initializing cookies.")

            response[self.cookie_name] = 0
            return self.SetCookie(response)

    def post(self):

        response = {}

        if request.cookies.get(self.cookie_name):

            response['status'] = 200
            response[self.cookie_name] = int(request.cookies.get(self.cookie_name)) + 1
        
            self.logger.info(f"Updating cookies: {response['status']}")
            return self.SetCookie(response)
            
        response['status'] = 404
        response['error'] = "Cookies not found"
        
        self.logger.info(f"Cookies not found: {response}")

        return jsonify(response)
    
    def SetCookie(self, response):

        #   Set the cookie
        resp = make_response(jsonify(response))
        resp.set_cookie(self.cookie_name, str(response[self.cookie_name]))
        return resp
