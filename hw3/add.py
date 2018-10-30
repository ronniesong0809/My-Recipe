"""
add a new recipe to sqlite
"""
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Add(MethodView):
    def get(self):
        return render_template('add.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['title'],
                     request.form['author'], 
                     request.form['ingredient'],
                     request.form['time'],
                     request.form['skill'],
                     request.form['description'])
        return redirect(url_for('index'))
