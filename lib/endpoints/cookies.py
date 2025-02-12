#   Flask Cookies
from flask.views import MethodView
from flask import request, render_template, make_response

from lib.config.logger import CookieWatcher

class Cookies(MethodView):

    def __init__(self):
        self.cookie = CookieWatcher()
        self.cookie.setup("Cookie.log")

    def get(self):

        click = None
        if request.cookies.get("Click(s)"):
            click = request.cookies.get("Click(s))")
            self.cookie.log.info(f"Click(s): {click}")
        
        if not click:
            click = 0
        return render_template("index.html", count= int(click))
    
    def post(self):

        click = request.cookies.get("Click(s)")
        resp = make_response(render_template("index.html"))
        resp.set_cookie("Click(s)", f"{int(click) + 1}")
        self.cookie.log.info(f"Click(s): {click}")

        return resp