"""
A recipes flask app dervied from guestbook-v3 app
"""
import flask
from flask.views import MethodView
from home import Home
from index import Index
from add import Add
from remove import Remove

app = flask.Flask(__name__)

"""
route method of flask with '/' as landing page
"""
app.add_url_rule('/',
                 view_func=Home.as_view('home'),
                 methods=['GET'])
"""
route method of flask with '/add' as the page to list all recipes
"""
app.add_url_rule('/index/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

"""
route method of flask with '/add' as the page to add recipe
"""
app.add_url_rule('/add/',
                 view_func=Add.as_view('add'),
                 methods=['GET', 'POST'])
                 
"""
route method of flask with '/remove' as the page to remove recipe
"""
app.add_url_rule('/remove/',
                 view_func=Remove.as_view('remove'),
                 methods=['GET', 'POST'])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


