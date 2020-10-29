"""
route method of flask with '/add' as the page to list all recipes
"""
from flask import render_template
from flask.views import MethodView
from google.cloud import translate
from google.cloud import vision
import requests
import gbmodel
import os

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()

        """dictionary of list and sqlite."""
        lang1='zh'
        lang2='ru'

        recipes = [dict(title=row[0],
                        author=row[1],
                        ingredient=row[2],
                        time=row[3],
                        skill=row[4],
                        description=row[5],
                        url=row[6],
                        url_description=self.detect_labels_uri(row[6]),
                        t_title=row[7],
                        t_author=row[8],
                        t_ingredient=row[9],
                        t_time=row[10],
                        t_skill=row[11],
                        t_description=row[12],
                        t2_title=row[0],
                        t2_author=row[1],
                        t2_ingredient=row[2],
                        t2_time=row[3],
                        t2_skill=row[4],
                        t2_description=row[5],
                        nutrition = self.nutritionix(row[2]),
                        yelp = self.yelpSearch(row[0])) for row in model.select()]

        return render_template('index.html', rps=recipes)

    # google cloud translate api
    def translate(self,text,target):
        translate_client = translate.Client()

        result = translate_client.translate(text,target_language=target)

        return result['translatedText']

    # google cloud translate api
    def detect_labels_uri(self,uri):

        if not uri:
            return "['No label']"

        else:
            client = vision.ImageAnnotatorClient()

            image = vision.types.Image()
            image.source.image_uri = uri

            response = client.label_detection(image=image)
            labels = response.label_annotations

            label_descriptions=[]
            for label in labels:
                label_descriptions.append(label.description)

            return label_descriptions

    # nutritionix api
    def nutritionix(self, ingredient):
        # url
        url = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

        # header
        headers = {"Content-Type":"application/json", "x-app-id":os.environ.get("X_APP_ID"), "x-app-key":os.environ.get("X_APP_KEY")}

        # body
        body = {"query":ingredient,"timezone": "US/Eastern"}

        # response object
        response = requests.post(url, headers= headers, json = body)

        # returns a promise that resolves with the result of parsing the body text as json 
        return response.json()

    # yelp api
    def yelpSearch(self, title):
        # url
        url = 'https://api.yelp.com/v3/businesses/search?term=' + title + '&location=portland&limit=3'

        # header
        headers={'Authorization': os.environ.get("YELP_API_KEY")}

        # response object
        response = requests.get(url, headers=headers)

        # returns a promise that resolves with the result of parsing the body text as json 
        return response.json()
