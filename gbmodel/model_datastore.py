"""
Google Cloud Datastore model
"""
from .Model import Model
from google.cloud import datastore

def from_datastore(entity):
    """
    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ title, author, ingredient, time, skill, description ]
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['title'],entity['author'],entity['ingredient'],entity['time'],entity['skill'],entity['description']]

class model(Model):
    def __init__(self):
        self.client = datastore.Client('cs410c-ron-song')

    def select(self):
        query = self.client.query(kind = 'Recipe')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def insert(self,title,author,ingredient,time,skill,description):
        key = self.client.key('Recipe')
        rev = datastore.Entity(key)
        rev.update( {
            'title': title,
            'author': author,
            'ingredient' : ingredient,
            'time' : time,
            'skill' : skill,
            'description' : description
            })
        self.client.put(rev)
        return True
