from flask import Blueprint, render_template

# Blueprint instance to main route
main = Blueprint("main", __name__)


'''
INDEX ROUTE
'''


@main.route('/')
def index():
    return render_template("index.html")
