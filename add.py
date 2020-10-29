"""
add a new recipe to sqlite
"""
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
from google.cloud import translate
import gbmodel

class Add(MethodView):
    def get(self):
        return render_template('add.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """

        lang=request.form['lang']

        model = gbmodel.get_model()
        model.insert(request.form['title'],
                    request.form['author'],
                    request.form['ingredient'],
                    request.form['time']+" minutes",
                    request.form['skill'],
                    request.form['description'],
                    request.form['url'],
                    self.translate(request.form['title'], lang),
                    self.translate(request.form['author'], lang),
                    self.translate(request.form['ingredient'], lang),
                    self.translate(request.form['time']+" minutes", lang),
                    self.translate(request.form['skill'], lang),
                    self.translate(request.form['description'], lang))
        return redirect(url_for('index'))

    # google cloud translate api
    def translate(self,text,target):
        translate_client = translate.Client()

        result = translate_client.translate(text,target_language=target)

        return result['translatedText']