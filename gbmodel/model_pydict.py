"""
Python dictionary model
"""
from .Model import Model

class model(Model):
    def __init__(self):
        """ init the recipes dictionary and then calls function to insert hard-coded data to dictionary"""
        self.recipeset = {}
        self.hardcoded()
        
    def select(self):
        """ 
        Returns recipeset list of dictionary
        Each list in recipeset contains: title, author, ingredient, time, skill, description
        :return: List of lists
        """
        return self.recipeset

    def insert(self, title, author, ingredient, time, skill, description):
        """
        Appends a new list of values representing new message into recipeset
        :param title: String
        :param author: String
        :param ingredient: String
        :param time: String
        :param skill: String
        :param description: String
        :return: True
        """
        self.recipeset[title] ={"title":title, "author":author, "ingredient":ingredient, "time":time, "skill":skill, "description":description}
        return True

    def hardcoded(self):
        self.recipeset["Spicy Grilled Eggplant"] ={"title":"Spicy Grilled Eggplant", "author":"Greg Fontenot", "ingredient":"Eggplant, oliver oil, lime juice", "time":"20 minutes", "skill":"Easy", "description":"This grilled side goes well with pasta or meats also made on the grill. Thanks to the Cajun seasoning, it gets more attention than an ordinary veggie"}
        self.recipeset["Pan-seared Strip Steak"] ={"title":"Pan-seared Strip Steak", "author":"Robin Bashinsky", "ingredient":"New york strip steak, salt, peper, oliver oil, butter", "time":"30 minutes", "skill":"Easy", "description":"Perfect dinner for meat lover!"}
        self.recipeset["Italian Mushrooms"] ={"title":"Italian Mushrooms", "author":"Kim Reichert", "ingredient":"1 pound Fresh mushrooms, onion, butter, italian salad dressing", "time":"4 hours", "skill":"Easy", "description":"Only four ingredients create a rich and flavorful side dish that we love to eat with beef and mashed potatoes"}
        self.recipeset["Turkey Saltimbocca"] ={"title":"Turkey Saltimbocca", "author":"Deirdre Cox", "ingredient":"1/4 cup flour, turkey breast tenderloin, peper, oliver oil, butter, 1 thin slice ham, 1/4 chicken broth", "time":"30 minutes", "skill":"Easy", "description":"I kept prosciutto and sage in this Italian classic, but instead of veal I added turkey. This Saltimbocca is so divine, you wont believe how quick and easy it is"}
        self.recipeset["Maple-Thyme Chicken Thighs"] ={"title":"Maple-Thyme Chicken Thighs", "author":"Lorraine Caland", "ingredient":"2 tsp ground mustard, 2 tsp maple syrup, salt, pepper, 6 chicken thighs", "time":"15 minutes", "skill":"Easy", "description":"We eat a lot of chicken at our house, and figuring out different ways to serve it gets challenging. My family went nuts for the cozy maple flavors in this recipe, so now I share it at potlucks, too"}
        self.recipeset["Southwest Beef & Rice Skillet"] ={"title":"Southwest Beef & Rice Skillet", "author":"Jane Porras", "ingredient":"1 cup rice, 1 pound ground beef, onion garlic", "time":"25 minutes", "skill":"Easy", "description":"My family loves this recipe because it’s so tasty, fast and filling. I love the easy one-dish cleanup. Sometimes I add a can of drained corn for a complete meal"}
        return True
