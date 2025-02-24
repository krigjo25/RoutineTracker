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

        click = str(request.cookies.get("Click(s))")) if request.cookies.get("Click(s)") else 0

        self.logger.warn(request.headers)
        self.logger.info(f"Click(s): {click}")
        return render_template("index.html", click= click)
    
    def post(self):

        click = request.cookies.get("Click(s)")
        resp = make_response()
        resp.set_cookie("Click(s)", f"{click}")
        
        self.logger.warn(request.headers)
        self.logger.info(f"Click(s): {click}")


        return make_response(render_template('index.html',click = click), 200)
