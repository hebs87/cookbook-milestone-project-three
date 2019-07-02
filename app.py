import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Instance of Flask
app = Flask(__name__)

# Config Flask app and connect to database
app.config["MONGO_DBNAME"] = 'onlineCookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

# Instance of PyMongo
mongo = PyMongo(app)

# DB collection variables
recipes_coll = mongo.db.recipes
rating_coll = mongo.db.ratings
categories_coll = mongo.db.categories
serves_coll = mongo.db.serves
time_coll = mongo.db.time
users_coll = mongo.db.userLogin

@app.route('/')
def base():
    return render_template("base.html")

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=recipes_coll.find())

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=False)