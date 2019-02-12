"""
remove a exist recipe from sql database, its not nesscarry for hw3 but i would like to have it for pratice
"""
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Remove(MethodView):
    def get(self):
        return render_template('remove.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.remove(request.form['title'])
        return redirect(url_for('index'))
