"""
Base Model
"""
class Model():
    def select(self):
        """
        Gets all recipes from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, title, author, ingredient, time, skill, description, url):
        """
        Inserts recipe into database
        :param title: String
        :param author: String
        :param ingredient: String
        :param time: String
        :param skill: String
        :param description: String
        :param url: String
        :return: True
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass
