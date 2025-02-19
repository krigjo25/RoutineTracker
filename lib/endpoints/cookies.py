#   Flask Cookies
from flask.views import MethodView
from flask import request, jsonify, make_response, render_template

from lib.config.logger import CookieWatcher

#   Initialize the logger
logger = CookieWatcher()
logger.FileHandler()

class Cookies(MethodView):

    def __init__(self, *args, **kwargs):
        self.logger = logger

    def get(self):
        cookie_clicks = 0
        cookie_name = "Count"
    
        if request.cookies.get(cookie_name):
            cookie_clicks = int(request.cookies.get(cookie_name))

            self.logger.info(f"Cookie found: {cookie_clicks}")
            return self.defineCookie(cookie_name, cookie_clicks)

        
        self.logger.warn(f"Cookies not found {request.cookies}")


        return self.defineCookie(cookie_name, cookie_clicks)

    
    def post(self):

        data = request.get_json()

        for key, value in data.items():
            print(key, value)
        
        for key, value in data.items():

            self.logger.info(f"Json requested: {key} : {value}")

            if request.cookies.get(key):
                click = int(value) + 1

                self.logger.info(f"Coo: {click}")

                return self.defineCookie(key, click)

    def defineCookie(self, name, click:int):

        response = {}
        response["message"] = "Cookie set"
        response["status"] = "200"
        response["count"] = click
        resp = make_response(jsonify(response))
        resp.set_cookie(name,  str(click))

        self.logger.info(f"Cookie set: {resp}")
        return resp
    
    def deleteCookies(self, name):
        resp = make_response(render_template("index.html", count=0))
        resp.set_cookie(name, 0)
        return resp