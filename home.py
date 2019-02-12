"""
the landing page for recipe app.
"""
from flask import render_template
from flask.views import MethodView
import gbmodel

class Home(MethodView):
    def get(self):
        return render_template('home.html')
