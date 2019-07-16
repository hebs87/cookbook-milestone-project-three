import os, json, math, html
import re
from flask import Flask, render_template, redirect, request, session, g, url_for, flash, Markup
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import date
from flask_uploads import UploadSet, configure_uploads, IMAGES

# Instance of Flask
app = Flask(__name__)

# Config for storing uploaded images
images = UploadSet('images', IMAGES)
app.config["UPLOADED_IMAGES_DEST"] = "static/img"
configure_uploads(app, images)

# Config Flask app and connect to database
app.config["MONGO_DBNAME"] = 'onlineCookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')
# Secret key to enable user sessions for login and flash messages - generates random string
app.secret_key = os.urandom(24)

# Instance of PyMongo
mongo = PyMongo(app)

# DB collection variables
recipes_coll = mongo.db.recipes
rating_coll = mongo.db.rating
categories_coll = mongo.db.categories
serves_coll = mongo.db.serves
time_coll = mongo.db.time
types_coll = mongo.db.types
occasions_coll = mongo.db.occasions
cuisines_coll = mongo.db.cuisines
main_ing_coll = mongo.db.main_ing
users_coll = mongo.db.userLogin

# Functions for drop down menus (called multiple times in other functions)
def rating_dropdown():
    '''
    Drop down menu for rating values
    Accesses rating array within the rating database
    '''
    return [
        r for rating in rating_coll.find()
        for r in rating.get("rating")]

def time_dropdown():
    '''
    Drop down menu for time values (prep time and cook time)
    Accesses time array within the time database
    '''
    return [
        t for time in time_coll.find()
        for t in time.get("time")]

def serves_dropdown():
    '''
    Drop down menu for serves values (how many people the recipe serves)
    Accesses serves array within the serves database
    '''
    return [
        s for serves in serves_coll.find()
        for s in serves.get("serves")]

# def types_dropdown():
#     '''
#     Drop down menu for types values
#     Accesses types array within the types database
#     '''
#     return [
#         t for types in types_coll.find()
#         for t in types.get("types")]

# def occasions_dropdown():
#     '''
#     Drop down menu for occasions values
#     Accesses occasions array within the occasions database
#     '''
#     return [
#         o for occ in occasions_coll.find()
#         for o in occ.get("occasions")]

# def cuisines_dropdown():
#     '''
#     Drop down menu for cusines values
#     Accesses cusines array within the cusines database
#     '''
#     return [
#         c for cuisine in cuisines_coll.find()
#         for c in cuisine.get("cuisines")]

# def main_ing_dropdown():
#     '''
#     Drop down menu for main_ing values
#     Accesses main_ing array within the main_ing database
#     '''
#     return [
#         m for main in main_ing_coll.find()
#         for m in main.get("main_ing")]

def categories_dropdown(key, val):
    '''
    Drop down menu for categories values (type, occasion, cuisine & main_ing
    These are arrays that are nested within the categories object in the database
    The function uses the key, val parameters to access the relevant nested array
    '''
    for c in categories_coll.find():
        return c[key][val]
    
# Other global variables (called in multiple functions)
rating_list = rating_dropdown()
time_list = time_dropdown()
serves_list = serves_dropdown()
types_list = categories_dropdown('categories', 'type')
occasions_list = categories_dropdown('categories', 'occasion')
cuisines_list = categories_dropdown('categories', 'cuisine')
main_ing_list = categories_dropdown('categories', 'main_ing')

# Other helper functions (called multiple times in other functions)

def find_recipe(recipe_id):
    '''
    Finds the receipe details based on the recipe_id
    '''
    return recipes_coll.find_one({"_id": ObjectId(recipe_id)})

# Route to index.html
@app.route('/')
def index():
    return render_template("index.html")

'''
USER LOGIN AND LOGOUT FUNCTIONALITY
'''

@app.route('/login_register')
def login_register():
    return render_template("login_register.html")
    
@app.route('/login', methods=["GET", "POST"])
def login():
    '''
    Login
    Checks that the user exists, and that user's password matches the
    hased password in the database
    '''
    if request.method == "POST":
        
        username = request.form.get('username').lower()
        password = request.form.get("password")
        existing_user = users_coll.find_one({"username": username})
        
        # Check if username exists and user's password matches the hashed password
        if existing_user and check_password_hash(existing_user["password"], password):
            flash(Markup("Welcome back " + username + ", you're now logged in!"))
            session['user'] = username
            return redirect(url_for('index'))
        # If either the username or password don't match, generic flash message is displayed
        else:
            flash(Markup("It appears those details don't match what we have, please try again."))
            return redirect(url_for('login'))
            
    return render_template("login_register.html")

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
                flash(Markup("Usernames must be alphanumeric only. Please try another one."))
                return redirect(url_for('register'))
        for letter in new_password:
            if not letter.isalnum():
                flash(Markup("Passwords must be alphanumeric only. Please try another one."))
                return redirect(url_for('register'))
        
        # Check username and password are between 6-15 characters
        if len(new_username) < 5 or len(new_username) > 15:
            flash(Markup("Usernames must be between 5 and 15 characters. Please try again."))
            return redirect(url_for('register'))
        if len(new_password) < 5 or len(new_password) > 15:
            flash(Markup("Passwords must be between 5 and 15 characters. Please try again."))
            return redirect(url_for('register'))
        
        # Check if username already exists
        existing_user = users_coll.find_one({"username": new_username})
        if existing_user:
            flash(Markup("Sorry, " + new_username + " is already taken! Please choose another one!"))
            return redirect(url_for('register'))
        
        # If all checks pass, add user to the database and hash the password
        users_coll.insert_one({
            "username": new_username,
            "password": generate_password_hash(new_password)
        })
        session['user'] = new_username
        flash(Markup("Welcome " + new_username + ", you're now logged in!"))
        return redirect(url_for('index'))
    
    return render_template("login_register.html")

@app.route('/logout')
def logout():
    '''
    Remove the session cookie and end the user session
    '''
    session.pop('user', None)
    flash(Markup("You were successfully logged out"))
    return redirect(url_for('index'))

@app.before_request
def before_request():
    '''
    Checks if the user is logged in before each request
    '''
    g.user = None
    if 'user' in session:
        g.user = session['user']

'''
CREATE OPERATION
'''

@app.route('/add_recipe')
def add_recipe():
    '''
    Return the add_recipe.html template and inject the data into drop down menus
    '''
    return render_template("add_recipe.html",
        rating=rating_list,
        time=time_list,
        serves=serves_list,
        types=types_list,
        occasions=occasions_list,
        cuisines=cuisines_list,
        main_ing=main_ing_list)

@app.route('/insert_recipe', methods=["GET", "POST"])
def insert_recipe():
    '''
    Insert the new recipe entry into the database
    '''
    if request.method == 'POST':
        # Check if user has submitted an image
        # If filepath field is an empty string, no image is present
        if request.form.get("filepath") != "":
            # If user has submitted a new image,
            # save to location and upload relative file path to database
            file_name = images.save(request.files['image'])
            file_path = "img/" + file_name
        else:
            # If no image, stock image file path will be stored in database
            file_path = "img/no-image-available.jpg"
        
        # Get today's date
        today = date.today()
        today_date = today.strftime("%d %B %Y")
        
        # Get session user details
        user = session['user'].lower()
        user_id = users_coll.find_one({"username": user})["_id"]
        
        insert = {
            "name": request.form.get("name").lower(),
            "rating_values": [
                int(request.form.get("rating"))
            ],
            "prep_time": request.form.get("prep_time").lower(),
            "cook_time": request.form.get("cook_time").lower(),
            "serves": request.form.get("serves").lower(),
            "ingredients": request.form.getlist("ingredients"),
            "instructions": request.form.getlist("instructions"),
            "categories": {
                "type": request.form.get("type").lower(),
                "occasion": request.form.get("occasion").lower(),
                "cuisine": request.form.get("cuisine").lower(),
                "main_ing": request.form.get("main_ing").lower(),
            },
            "author": request.form.get("author").lower(),
            "img": file_path,
            "added_by": user_id,
            "added_date": today_date,
            "last_edited_date": "",
            "views": 0,
            "deleted": False
        }
        
        # Insert recipe dict (insert variable) into the database
        recipes_coll.insert_one(insert)
        
        # Flash message confirmation that recipe has been successfully added
        flash(Markup("Thanks " + user.capitalize() + ", your recipe has been added!"))
        
        return redirect(url_for('get_recipes'))

'''
READ OPERATION
'''

@app.route('/get_recipes')
def get_recipes():
    '''
    Get all recipes and display summary details in cards
    '''
    recipes = recipes_coll.find()
    return render_template("browse.html", recipes=recipes)

@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    '''
    Gets details for a particular recipe_id that the user clicked on browse.html
    This routes the user to the recipes.html page with details for that recipe_id
    Each time the recipe is viewed, it increments the 'views' field in the DB by one
    '''
    recipe = find_recipe(recipe_id)
    
    # Increment 'views' field by 1 each time the recipe is viewed
    recipes_coll.update_one({"_id": ObjectId(recipe_id)}, {"$inc": {"views": 1}})
    
    # Convert added_by ObjectId to the username value - verify against the session user
    added_by = users_coll.find_one(
        {"_id": ObjectId(recipe.get("added_by"))})["username"]
        
    return render_template("recipes.html",
        recipe=recipe,
        ratings=rating_list,
        added_by=added_by)

'''
UPDATE OPERATION
'''

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    '''
    Route user to edit_recipe.html and inject existing data into the form
    Give users the ability to amend the recipe details
    '''
    recipe = find_recipe(recipe_id)
    
    return render_template("edit_recipe.html",
        recipe=recipe,
        ratings=rating_list,
        time=time_list,
        serves=serves_list,
        types=types_list,
        occasions=occasions_list,
        cuisines=cuisines_list,
        main_ing=main_ing_list)

@app.route('/update_recipe/<recipe_id>', methods=["POST"])
def update_recipe(recipe_id):
    '''
    Update existing database record with the new form values
    '''
    if request.method == 'POST':
        
        # Get the recipe_id
        recipe = find_recipe(recipe_id)
        
        # Convert added_by ObjectId to the username value - verify against the session user
        added_by = recipe.get("added_by")
        
        # Check if user has submitted an image
        if request.form.get("filepath") == recipe.get("img"):
            # If no new image is added by the user (URL unchanged)
            file_path = recipe.get("img")
        elif request.form.get("filepath") != "":
            # If user has submitted a new image,
            # save to location and upload relative file path to database
            file_name = images.save(request.files['image'])
            file_path = "img/" + file_name
        else:
            # If user removes the image, stock image file path will be stored in database
            file_path = "img/no-image-available.jpg"
        
        # Get rating values
        rating_values = recipe.get("rating_values")
        
        # Get added date
        added_date = recipe.get("added_date")
        
        # Get last edited date
        today = date.today()
        last_edited_date = today.strftime("%d %B %Y")
        
        # Get number of views and decrement by 1
        # Resolves bug of it being incremented when redirected to recipes.html
        views = recipe.get("views")
        decrement_views = views - 1
        
        # Get session user details
        user = session['user'].capitalize()
        
        # Update new values in the database
        recipes_coll.update({"_id": ObjectId(recipe_id)}, {
            "name": request.form.get("name").lower(),
            "rating_values": rating_values,
            "prep_time": request.form.get("prep_time").lower(),
            "cook_time": request.form.get("cook_time").lower(),
            "serves": request.form.get("serves").lower(),
            "ingredients": request.form.getlist("ingredients"),
            "instructions": request.form.getlist("instructions"),
            "categories": {
                "type": request.form.get("type").lower(),
                "occasion": request.form.get("occasion").lower(),
                "cuisine": request.form.get("cuisine").lower(),
                "main_ing": request.form.get("main_ing").lower(),
            },
            "author": request.form.get("author").lower(),
            "img": file_path,
            "added_by": added_by,
            "added_date": added_date,
            "last_edited_date": last_edited_date,
            "views": decrement_views,
            "deleted": False
        })
        
        
        
        # Flash message confirmation that recipe has been successfully added
        flash(Markup("Thanks " + user.capitalize() + ", this recipe has been successfully edited!"))
        
        return redirect(url_for('recipe',
            recipe_id=recipe_id))

'''
DELETE OPERATION
'''
@app.route('/remove_recipe/<recipe_id>')
def remove_recipe(recipe_id):
    '''
    Changes the 'deleted' in the recipes collection to 'True' when the user deletes the recipe
    This ensures that the recipe remains in the database but is removed from the front end
    '''
    # Change the deleted field to 'True'
    recipes_coll.update_one({"_id": ObjectId(recipe_id)}, {"$set": {"deleted": True}})
    
    # Get session user details
    user = session['user'].capitalize()
    
    # Flash message confirmation that recipe has been successfully added
    flash(Markup("Thanks " + user.capitalize() + ", this recipe has been successfully deleted!"))
    
    return redirect(url_for('get_recipes',
        recipe_id=recipe_id))

@app.route('/rate/<recipe_id>', methods=["GET", "POST"])
def rate(recipe_id):
    '''
    Allows the user to rate the recipe
    Pushes the rating value into the rating_values list in the recipes collection
    '''
    # Push rating from form into the rating_values field in the relevant record
    recipes_coll.update_one({"_id": ObjectId(recipe_id)},
        {"$push": {"rating_values": int(request.form.get("rating"))}})
    
    # Decrement number of views by 1
    # Resolves bug of it being incremented when redirected to recipes.html
    recipes_coll.update_one({"_id": ObjectId(recipe_id)},
        {"$inc": {"views": -1}})
    
    
    # Flash message confirmation that recipe has been successfully added
    flash(Markup("Thanks for rating this recipe!"))
    
    return redirect(url_for('recipe',
            recipe_id=recipe_id))

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=False)