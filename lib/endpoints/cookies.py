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
        if request.cookies.get("Click(s)"):
            click = str(request.cookies.get("Click(s))")) if request.cookies.get("Click(s)") else 0
        
        if click is None:
            click = 0
        
        self.logger.info(f"Click(s): {click}")
        
        if not click:
            click = 0
        return jsonify("clicks", click)
    
    def post(self):

        click = request.cookies.get("Click(s)")
        resp = make_response()
        resp.set_cookie("Click(s)", f"{click}")
        self.logger.log.info(f"cookie: {click}")

        return make_response(jsonify({'clicks': click}), 200)
