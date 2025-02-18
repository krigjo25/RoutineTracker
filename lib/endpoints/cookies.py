#   Flask Cookies
from flask.views import MethodView
from flask import request, jsonify, make_response, render_template

from lib.config.logger import CookieWatcher

#   Initialize the logger
logger = CookieWatcher()
logger.ConsoleHandler()

class Cookies(MethodView):

    def __init__(self, *args, **kwargs):
        self.logger = logger

    def get(self):
        clicks = 0
        cookie_name = "Count"
        response = {}
    
        if request.cookies.get(cookie_name):
            clicks = int(request.cookies.get(cookie_name))

            self.logger.info(f"Cookie found: {clicks}")

            return self.defineCookie(cookie_name, clicks)

        
        self.logger.warn(f"Cookies not found {request.cookies}")
        return jsonify({"message": "Cookies not found"})

    
    def post(self):

        click = 0
        name = "Count"

        if request.cookies.get(name):
            click = int(request.cookies.get(name)) + 1

            return self.defineCookie(name, click)
        else:
            return render_template("index.html", count=click)

    def defineCookie(self, name, click):

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