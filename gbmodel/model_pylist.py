"""
Python list model
"""
from datetime import date
from .Model import Model

class model(Model):
    def __init__(self):
        self.recipeset = []
        self.hardcoded()        

    def select(self):
        """
        Returns recipeset list of lists
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
        params = [title, author, ingredient, time, skill, description]
        self.recipeset.append(params)
        return True

    def harcoded(self)
        self.recipeset.append(['Spicy Grilled Eggplant', 'Greg Fontenot', 'Eggplant, oliver oil, lime juice,', '20 minutes', 'Easy', 'This grilled side goes well with pasta or meats also made on the grill. Thanks to the Cajun seasoning, it gets more attention than an ordinary veggie'])
        self.recipeset.append(['Pan-seared Strip Steak', 'Robin Bashinsky', 'New york strip steak, salt, peper, oliver oil, butter', '30 minutes', 'Easy', 'Perfect dinner for meat lover!'])
        self.recipeset.append(['Italian Mushrooms', 'Kim Reichert', '1 pound Fresh mushrooms, onion, butter, italian salad dressing', '4 hours', 'Easy', 'Only four ingredients create a rich and flavorful side dish that we love to eat with beef and mashed potatoes'])
        self.recipeset.append(['Turkey Saltimbocca', 'Deirdre Cox', '1/4 cup flour, turkey breast tenderloin, peper, oliver oil, butter, 1 thin slice ham, 1/4 chicken broth', '30 minutes', 'Easy', 'I kept prosciutto and sage in this Italian classic, but instead of veal I added turkey. This Saltimbocca is so divine, you wont believe how quick and easy it is'])
        self.recipeset.append(['Maple-Thyme Chicken Thighs', 'Lorraine Caland', '2 tsp ground mustard, 2 tsp maple syrup, salt, pepper, 6 chicken thighs', '15 minutes', 'Easy', 'We eat a lot of chicken at our house, and figuring out different ways to serve it gets challenging. My family went nuts for the cozy maple flavors in this recipe, so now I share it at potlucks, too'])
        self.recipeset.append(['Southwest Beef & Rice Skillet', 'Jane Porras', '1 cup rice, 1 pound ground beef, onion garlic', '25 minutes', 'Easy', 'My family loves this recipe because it’s so tasty, fast and filling. I love the easy one-dish cleanup. Sometimes I add a can of drained corn for a complete meal'])
        return True
