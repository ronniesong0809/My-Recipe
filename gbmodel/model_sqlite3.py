"""
A recipes flask webapp that derive from guestbook.
ata is stored in a SQLite database that looks something like the following:

+-------+----------+---------------------------+---------+--------------+-----------------------------------------------------------+
| Title | Author   | Ingredient                | Time    | Skill Level  | Description                                               |
+=======+==========+===========================+=========+==============+===========================================================+
| Steak | John Doe | Round Steak, Salt, Pepper | 10 mins | Intermediate | Cook for 1 minute each side in a large cast iron skullet. |
+-------+----------+---------------------------+---------+--------------+-----------------------------------------------------------+

This can be created with the following SQL (see bottom of this file):

    create table recipes (title text, author text, ingredient text, time text, skill text, description);

"""
from datetime import date
from .Model import Model
import sqlite3
DB_FILE = 'recipes.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from recipes")
        except sqlite3.OperationalError:
            cursor.execute("create table recipes (title text, author text, ingredient text, time text, skill text, description, url text, t_title text, t_author text, t_ingredient text, t_time text, t_skill text, t_description)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: title, author, ingredient, time, skill, description
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM recipes")
        return cursor.fetchall()

    def insert(self, title, author, ingredient, time, skill, description, url, t_title, t_author, t_ingredient, t_time, t_skill, t_description):
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
        :raises: Database errors on connection and insertion
        """
        params = {'title':title, 'author':author, 'ingredient':ingredient, 'time':time, 'skill':skill, 'description':description, 'url':url, 't_title':t_title, 't_author':t_author, 't_ingredient':t_ingredient, 't_time':t_time, 't_skill':t_skill, 't_description':t_description}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into recipes (title, author, ingredient, time, skill, description, url, t_title, t_author, t_ingredient, t_time, t_skill, t_description) VALUES (:title, :author, :ingredient, :time, :skill, :description, :url, :t_title, :t_author, :t_ingredient, :t_time, :t_skill, :t_description)", params)

        connection.commit()
        cursor.close()
        return True

    def remove(self, title):
        """
        remove recipe from database
        :param title: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'title':title}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("delete from recipes where title = :title", params)

        connection.commit()
        cursor.close()
        return True
