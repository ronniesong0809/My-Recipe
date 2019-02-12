"""
route method of flask with '/add' as the page to list all recipes
"""
from flask import render_template
from flask.views import MethodView
from google.cloud import translate
from google.cloud import vision
import requests
import gbmodel

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
                        t_title=self.translate(row[0],lang1),
                        t_author=self.translate(row[1],lang1),
                        t_ingredient=self.translate(row[2],lang1),
                        t_time=self.translate(row[3],lang1),
                        t_skill=self.translate(row[4],lang1),
                        t_description=self.translate(row[5],lang1),
                        t2_title=self.translate(row[0],lang2),
                        t2_author=self.translate(row[1],lang2),
                        t2_ingredient=self.translate(row[2],lang2),
                        t2_time=self.translate(row[3],lang2),
                        t2_skill=self.translate(row[4],lang2),
                        t2_description=self.translate(row[5],lang2),
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
        headers = {"Content-Type":"application/json", "x-app-id":"ec32a59d", "x-app-key":"d13ec612386c8937ed513fc295ad10e3"}
        
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
        headers={'Authorization': "Bearer T7zsAtPs89Md-UJVSSUpzGGPxljUmlU914d994tSlhL5v98RnTEmDvPEfHgwwNp5FooWOpWp45ciFSX2ON8HnDFRbojwEBMbyW1SslpL9VcL3o2gAwvLTXFBW-7rW3Yx"}
        
        # response object
        response = requests.get(url, headers=headers)
        
        # returns a promise that resolves with the result of parsing the body text as json 
        return response.json()
