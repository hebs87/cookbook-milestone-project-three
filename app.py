import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Instance of Flask
app = Flask(__name__)

# Config Flask app and connect to database
app.config["MONGO_DBNAME"] = 'onlineCookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

# Instanse of PyMongo
mongo = PyMongo(app)

@app.route('/')

@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=mongo.db.recipes.find())

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=False)