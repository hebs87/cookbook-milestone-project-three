import os, json, math
import re
from flask import Flask, render_template, redirect, request, session, g, url_for, flash, Markup
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash

# Instance of Flask
app = Flask(__name__)

# Config Flask app and connect to database
app.config["MONGO_DBNAME"] = 'onlineCookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
# Secret key to enable user sessions for login and flash messages - generates random string
app.secret_key = os.urandom(24)

# Instance of PyMongo
mongo = PyMongo(app)

# DB collection variables
recipes_coll = mongo.db.recipes
rating_coll = mongo.db.ratings
categories_coll = mongo.db.categories
serves_coll = mongo.db.serves
time_coll = mongo.db.time
users_coll = mongo.db.userLogin

# User login sessions/logout
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():
    return ''

@app.route('/register', methods=["GET", "POST"])
def register():
    '''
    Create new user/register new account
    Checks that the user doesn't already exist, and that length of username
    and password is between 6-15 characters
    Uses generate_password_hash to hash user's password in the database
    '''
    if request.method == "POST":
        
        new_username = request.form.get('new_username').lower()
        new_password = request.form.get("new_password")
        
        # Check username and password are alphanumeric
        for letter in new_username:
            if not letter.isalnum():
                message = "Usernames must be alphanumeric only. Please try another one."
                return message
        for letter in new_password:
            if not letter.isalnum():
                message = "Passwords must be alphanumeric only. Please try another one."
                return message
        
        # Check username and password are between 6-15 characters
        if len(new_username) < 5 or len(new_username) > 15:
            message = "Usernames must be between 5 and 15 characters. Please try again."
            return message
        if len(new_password) < 5 or len(new_password) > 15:
            message = "Passwords must be between 5 and 15 characters. Please try again."
            return message
        
        # Check if username already exists
        existing_user = users_coll.find_one({"username": new_username})
        if existing_user:
            message = "Sorry, " + new_username + " is already taken! Please choose another one!"
            return message
        
        # If all checks pass, add user to the database
        users_coll.insert_one({
            "username": new_username,
            "password": generate_password_hash(new_password)
        })
        session['user'] = new_username
        message = "Welcome " + new_username + ", you will now be logged in"
        return message
    
@app.route('/get_recipes')
def get_recipes():
    return render_template("recipes.html", recipes=recipes_coll.find())

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=False)