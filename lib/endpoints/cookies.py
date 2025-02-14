#   Flask Cookies
from flask.views import MethodView
from flask import request, jsonify, make_response, render_template

from lib.config.logger import CookieWatcher

class Cookies(MethodView):

    def __init__(self, *args, **kwargs):
        self.logger = CookieWatcher()
        self.logger.ConsoleHandler()

    def get(self):
        clicks = 0
        cookie_name = "Count"

        if request.cookies.get(cookie_name):
            clicks = int(request.cookies.get(cookie_name))


        return self.defineCookie(cookie_name, clicks)
    
    def post(self):

        click = 0
        name = "Count"

        if request.cookies.get(name):
            click = int(request.cookies.get(name)) + 1
        
            return self.defineCookie(name, click)

        if request.headers.get("reset"):

            self.deleteCookies(name)
            return render_template("index.html", count=click)

        else:
            return render_template("index.html", count=click)

    def defineCookie(self, name, click):

        resp = make_response(render_template("index.html", count=click))
        resp.set_cookie(name,  str(click))
        return resp
    
    def deleteCookies(self, name):
        resp = make_response(render_template("index.html", count=0))
        resp.set_cookie(name, 0)
        return resp