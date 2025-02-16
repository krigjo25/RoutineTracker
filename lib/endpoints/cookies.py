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

        if request.cookies.get(cookie_name):
            clicks = int(request.cookies.get(cookie_name))

            self.logger.info(f"Cookie found: {clicks}")
            return self.defineCookie(cookie_name, clicks)
        self.logger.warn("Cookies not found", request.cookies)
        return render_template("index.html", count=clicks)

    
    def post(self):

        click = 0
        name = "Count"

        if request.cookies.get(name):
            click = int(request.cookies.get(name)) + 1

            return self.defineCookie(name, click)
        else:
            return render_template("index.html", count=click)

    def defineCookie(self, name, click):

        resp = make_response(render_template("index.html", count=click))
        resp.set_cookie(name,  str(click))

        self.logger.info(f"Cookie set: {resp}")
        return resp
    
    def deleteCookies(self, name):
        resp = make_response(render_template("index.html", count=0))
        resp.set_cookie(name, 0)
        return resp