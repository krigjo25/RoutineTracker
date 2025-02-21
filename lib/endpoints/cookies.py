#   Flask Cookies
from flask.views import MethodView
from lib.config.logger import CookieWatcher
from flask import request, jsonify, make_response, render_template

#   Initialize the logger
logger = CookieWatcher()
logger.FileHandler()

class Cookies(MethodView):

    def __init__(self, *args, **kwargs):
        self.logger = logger

    def get(self):
        cookie_clicks = 0
        cookie_name = "count"

        if request.cookies.get(cookie_name):
            cookie_clicks = int(request.cookies.get(cookie_name))

            self.logger.info(f"Cookie found: {cookie_clicks}")
            return self.defineCookie(cookie_name, cookie_clicks)

        
        self.logger.warn(f"Cookies not found {request.cookies}")


        return self.defineCookie(cookie_name, cookie_clicks)

    def post(self):

        click = 0
        data = request.get_json()

        for key, value in data.items():
            print(key, value)

        self.logger.info(request.cookies.get("count"))

        return self.defineCookie(key, str(click))

    def defineCookie(self, name, click):

        response = {}
        response["status"] = "200"
        response["count"] = click
        response["message"] = "Cookie set"

        resp = make_response(jsonify(response))
        resp.set_cookie(name,  str(click))

        self.logger.info(f"Cookie set: {name} : {click}")
        return resp