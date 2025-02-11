#   Flask Cookies
from flask import request
class Cookies(object):

    def __init__(self):
        self.Click = request.cookies.get("Clicks")

    def get(self):
        response = {}
        ckicks = ""

        if request.cookies.get("Clicks"):
            self.click = request.cookies.get("Clicks")

        response["Clicks"] = self.click

        return response