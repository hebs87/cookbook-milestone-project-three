import os, json, math, html, pymongo
import re
from flask import Flask, render_template, redirect, request, session, g, url_for, flash, Markup
from flask_pymongo import PyMongo, pymongo
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

def get_username(username):
    '''
    Finds the username based on the session user
    '''
    return users_coll.find_one({"username": username.lower()})

'''
INDEX ROUTE
'''

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
    hashed password in the database
    '''
    if request.method == "POST":
        
        username = request.form.get('username').lower()
        password = request.form.get("password")
        existing_user = users_coll.find_one({"username": username})
        
        # Check if username exists and user's password matches the hashed password
        if existing_user and check_password_hash(existing_user["password"], password):
            flash(Markup("Welcome back \
                        <span class='message-helper bold italic'>" + username.capitalize() + "</span>, \
                        you're now logged in!"))
            session["user"] = username
            return redirect(url_for('index', username=session["user"]))
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
        # This won't be visible, as the min and max length are set in the HTML input fields
        if len(new_username) < 5 or len(new_username) > 15:
            flash(Markup("Usernames must be between 5 and 15 characters. Please try again."))
            return redirect(url_for('register'))
        if len(new_password) < 5 or len(new_password) > 15:
            flash(Markup("Passwords must be between 5 and 15 characters. Please try again."))
            return redirect(url_for('register'))
        
        # Check if username already exists
        existing_user = users_coll.find_one({"username": new_username})
        if existing_user:
            flash(Markup("Sorry, \
                        <span class='message-helper bold italic'>" + new_username.capitalize() + "</span> \
                        is already taken! Please choose another one."))
            return redirect(url_for('register'))
        
        # If all checks pass, add user to the database and hash the password
        users_coll.insert_one({
            "username": new_username,
            "password": generate_password_hash(new_password),
            "added_recipes": [],
            "liked_recipes": []
        })
        session["user"] = new_username
        flash(Markup("Thanks for signing up \
                    <span class='message-helper bold italic'>" + new_username.capitalize() + "</span>, \
                    you're now logged in!"))
        return redirect(url_for('index', username=session["user"]))
    
    return render_template("login_register.html")

@app.route('/logout')
def logout():
    '''
    Remove the session cookie and end the user session
    '''
    session.pop('user', None)
    flash(Markup("You were successfully logged out. Come back soon!"))
    return redirect(url_for('index'))

'''
USER'S PROFILE PAGE
'''

@app.route('/profile/<username>', methods=["GET", "POST"])
def profile(username):
    '''
    Loads the content on the user's profile page
    Gets the user's added and liked recipes
    '''
    username = get_username(session["user"])["username"]
    
    # Get all recipes from the recipes_coll that were added by the user's ID
    user_id = get_username(session["user"])["_id"]
    user_added_list = recipes_coll.find({'$and': [{"added_by": user_id},
                                        {"deleted": False}]}).sort([('name', 1)])
    
    # Get all recipes that the user has liked
    liked_recipes = get_username(session["user"])["liked_recipes"]
    user_liked_list = recipes_coll.find({"_id": {"$in": liked_recipes}}).sort([("name", 1)])
    
    return render_template("profile.html",
        username=username,
        user_added_list=user_added_list,
        user_liked_list=user_liked_list)

'''
CHANGE PASSWORD
'''

@app.route('/profile/<username>/change_password', methods=["POST"])
def change_password(username):
    '''
    Allows the user to change their password
    Users will have to enter their correct existing password first
    '''
    user = session["user"].lower()
    username = get_username(session["user"])
    existing_password = request.form.get("existing_password")
    changed_password = request.form.get("changed_password")
    
    # If stored password matches the entry, the password will be changed
    if check_password_hash(username["password"], existing_password):
        flash(Markup("Thanks \
                    <span class='message-helper bold italic'>" + user.capitalize() + "</span>, \
                    your password has successfully been changed!"))
        users_coll.update_one(
            {"username": user},
            {"$set": {"password": generate_password_hash(changed_password)}})
    # If stored password doesn't match the entry, generic flash message is displayed
    else:
        flash(Markup("Sorry \
                    <span class='message-helper bold italic'>" + user.capitalize() + "</span>, \
                    your existing password doesn't match what we have! Please try again."))
    
    return redirect(url_for('profile', username=username))

'''
DELETE ACCOUNT
'''

@app.route('/profile/<username>/delete_account', methods=["POST"])
def delete_account(username):
    '''
    Allows the user to delete their account
    Users will have to enter their correct existing password first
    Deleting the account will delete the user's recipes
    The user's recipes' deleted value will be updated to true and they will no longer be displayed
    The recipes will also be removed from all users' liked lists
    The user's details will be removed from the userLogin collection
    The session will end
    '''
    username = get_username(session["user"])
    confirm_password = request.form.get("confirm_password")
    user_upper = session["user"].capitalize()
    
    # If stored password matches the entry, the password will be changed
    if check_password_hash(username["password"], confirm_password):
        # Find the user's added recipes
        user_added_recipes = [recipe for recipe in username.get("added_recipes")]
        # Update the deleted value to true for each recipe from the recipes collection
        # Remove each recipe from the other users' liked list
        for recipe in user_added_recipes:
            recipes_coll.update_one({"_id": ObjectId(recipe)}, {"$set": {"deleted": True}})
            users_coll.update_many(
                {},
                {"$pull": {"liked_recipes": ObjectId(recipe)}})
        # Find the user's liked recipes
        user_liked_recipes = [recipe for recipe in username.get("liked_recipes")]
        # Decrement the likes field in each of those recipes by 1
        for recipe in user_liked_recipes:
            recipes_coll.update_one({"_id": ObjectId(recipe)}, {"$inc": {"likes": -1}})
        flash(Markup("Your account has been successfully deleted."))
        # End the user's session
        session.pop('user', None)
        # Remove the user's details from the userLogin collection
        users_coll.remove({"_id": username.get("_id")})
        # Redirect to index.html
        return redirect(url_for('index'))
    # If stored password doesn't match the entry, generic flash message is displayed
    else:
        flash(Markup("Sorry \
                    <span class='message-helper bold italic'>" + user_upper + "</span>, \
                    your existing password doesn't match what we have. please try again."))
    
    return redirect(url_for('profile', username=username))

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
            "likes": 0,
            "deleted": False
        }
        
        # Insert recipe dict (insert variable) into the database and get the new ID
        new_id = recipes_coll.insert_one(insert)
        
        # Add the new recipe ID to the users collection for that user
        users_coll.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {"added_recipes": new_id.inserted_id}})

        # Flash message confirmation that recipe has been successfully added
        flash(Markup("Thanks \
                    <span class='message-helper bold italic'>" + user.capitalize() + "</span>, \
                    your recipe has been added!"))
        
        return redirect(url_for('get_recipes', page=1))

'''
READ OPERATION
'''

@app.route('/get_recipes/<page>', methods=["GET", "POST"])
def get_recipes(page):
    '''
    Get all recipes and display summary details in cards
    '''
    # Number of results to skip when searching recipes collection - for pagination
    skip_count = (int(page) - 1) * 8
    
    # FILTERED RESULTS WITH NO SEARCH
    if request.method == 'POST':
        # Get the user's submission from the filter form and put into a dictionary
        form_input = request.form.to_dict()

        # Build the filter query
        # Error message if user doesn't select any filters before submitting form
        if len(form_input) == 0:
            flash(Markup("You haven't selected any filter options. Please choose a category to filter."))
            return redirect(url_for('get_recipes', page=1))

        # Filter query if one option is selected from the form
        elif len(form_input) == 1:
            for k, v in form_input.items():
                cat_one = 'categories.' + k
                val_one = v.lower()
                
                # Only include recipes with "deleted" value of False
                filter_query = ({'$and': [{cat_one: val_one},
                                {"deleted": False}]})

        # Filter query if two options are selected from the form
        elif len(form_input) == 2:
            if 'type' in form_input and 'occasion' in form_input:
                cat_one = 'categories.type'
                val_one = str(form_input['type']).lower()
                cat_two = 'categories.occasion'
                val_two = str(form_input['occasion']).lower()
            elif 'type' in form_input and 'cuisine' in form_input:
                cat_one = 'categories.type'
                val_one = str(form_input['type']).lower()
                cat_two = 'categories.cuisine'
                val_two = str(form_input['cuisine']).lower()
            elif 'type' in form_input and 'main_ing' in form_input:
                cat_one = 'categories.type'
                val_one = str(form_input['type']).lower()
                cat_two = 'categories.main_ing'
                val_two = str(form_input['main_ing']).lower()
            elif 'occasion' in form_input and 'cuisine' in form_input:
                cat_one = 'categories.occasion'
                val_one = str(form_input['occasion']).lower()
                cat_two = 'categories.cuisine'
                val_two = str(form_input['cuisine']).lower()
            elif 'occasion' in form_input and 'main_ing' in form_input:
                cat_one = 'categories.occasion'
                val_one = str(form_input['occasion']).lower()
                cat_two = 'categories.main_ing'
                val_two = str(form_input['main_ing']).lower()
            else:
                cat_one = 'categories.cuisine'
                val_one = str(form_input['cuisine']).lower()
                cat_two = 'categories.main_ing'
                val_two = str(form_input['main_ing']).lower()
            
            # Only include recipes with "deleted" value of False
            filter_query = ({'$and': [{cat_one: val_one},
                            {cat_two: val_two},
                            {"deleted": False}]})
            
        # Filter query if three options are selected from the form
        elif len(form_input) == 3:
            if 'type' in form_input and 'occasion' in form_input and 'cuisine' in form_input:
                cat_one = 'categories.type'
                val_one = str(form_input['type']).lower()
                cat_two = 'categories.occasion'
                val_two = str(form_input['occasion']).lower()
                cat_three = 'categories.cuisine'
                val_three = str(form_input['cuisine']).lower()
            elif 'type' in form_input and 'occasion' in form_input and 'main_ing' in form_input:
                cat_one = 'categories.type'
                val_one = str(form_input['type']).lower()
                cat_two = 'categories.occasion'
                val_two = str(form_input['occasion']).lower()
                cat_three = 'categories.main_ing'
                val_three = str(form_input['main_ing']).lower()
            elif 'type' in form_input and 'cuisine' in form_input and 'main_ing' in form_input:
                cat_one = 'categories.type'
                val_one = str(form_input['type']).lower()
                cat_two = 'categories.cuisine'
                val_two = str(form_input['cuisine']).lower()
                cat_three = 'categories.main_ing'
                val_three = str(form_input['main_ing']).lower()
            else:
                cat_one = 'categories.occasion'
                val_one = str(form_input['occasion']).lower()
                cat_two = 'categories.cuisine'
                val_two = str(form_input['cuisine']).lower()
                cat_three = 'categories.main_ing'
                val_three = str(form_input['main_ing']).lower()
            
            # Only include recipes with "deleted" value of False
            filter_query = ({'$and': [{cat_one: val_one},
                            {cat_two: val_two},
                            {cat_three: val_three},
                            {"deleted": False}]})
            
        # Filter query if all options are selected from the form
        elif len(form_input) == 4:
            cat_one = 'categories.type'
            val_one = str(form_input['type']).lower()
            cat_two = 'categories.occasion'
            val_two = str(form_input['occasion']).lower()
            cat_three = 'categories.cuisine'
            val_three = str(form_input['cuisine']).lower()
            cat_four = 'categories.main_ing'
            val_four = str(form_input['main_ing']).lower()
            
            # Only include recipes with "deleted" value of False
            filter_query = ({'$and': [{cat_one: val_one},
                            {cat_two: val_two},
                            {cat_three: val_three},
                            {cat_four: val_four},
                            {"deleted": False}]})
        
        recipes = recipes_coll.find(filter_query)
        
        # Pagination for filtered results
        paginated_recipes = recipes_coll.find(filter_query).sort([("likes", -1), 
                    ('name', 1), ("_id", 1)]).skip(skip_count).limit(8)
        
    # ALL RECIPES WITH NO SEARCH OR FILTERS
    else:
        # Only include recipes with "deleted" value of False
        recipes = recipes_coll.find({"deleted": False})
        
        # Pagination for all recipes
        paginated_recipes = recipes_coll.find({"deleted": False}).sort([("likes", -1), 
                    ('name', 1), ("_id", 1)]).skip(skip_count).limit(8)
    
    if recipes:
        recipes_count = recipes.count()
    else:
        recipes_count = 0
    
    total_pages = int(math.ceil(recipes_count/8.0))
    
    if recipes_count == 0:
        page = 0
    
    # RESULTS USING THE SEARCH FORM
    # Args variable to get args from the form
    args = request.args.get
    
    # Set search_word variable
    if args(str("search")):
        search_word = args(str("search"))
    else:
        search_word = ""

    if not search_word:
        search_results = ""
    else:
        # Only include recipes with "deleted" value of False
        search_results = recipes_coll.find(
                {'$and': [{"$text": {"$search": search_word}},
                {"deleted": False}]}).sort([("likes", -1), 
                ('name', 1)])

    # Count the search_results
    if search_results:
        search_results_count = search_results.count()
    else:
        search_results_count = 0
    
    return render_template("browse.html",
        page=page,
        recipes=paginated_recipes,
        recipes_count=recipes_count,
        search_results=search_results,
        search_results_count=search_results_count,
        total_pages=total_pages,
        types=types_list,
        occasions=occasions_list,
        cuisines=cuisines_list,
        main_ing=main_ing_list)

@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
    '''
    Gets details for a particular recipe_id that the user clicked on browse.html
    This routes the user to the recipes.html page with details for that recipe_id
    Each time the recipe is viewed, it increments the 'views' field in the DB by one
    '''
    recipe = find_recipe(recipe_id)
    
    try:
        # Get the user's liked_recipes list if a user is logged in
        user = session["user"].lower()
        liked_recipes = users_coll.find_one({"username": user})["liked_recipes"]
    except:
        # Create an empty liked_recipes list if no user is logged in
        liked_recipes = []
    
    # Increment 'views' field by 1 each time the recipe is viewed
    recipes_coll.update_one({"_id": ObjectId(recipe_id)}, {"$inc": {"views": 1}})
    
    # Convert added_by ObjectId to the username value - verify against the session user
    added_by = users_coll.find_one(
        {"_id": ObjectId(recipe.get("added_by"))})["username"]
        
    return render_template("recipes.html",
        recipe=recipe,
        ratings=rating_list,
        added_by=added_by,
        liked_recipes=liked_recipes)

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
        
        #Get number of likes
        likes = recipe.get("likes")
        
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
            "likes": likes,
            "deleted": False
        })
        
        # Flash message confirmation that recipe has been successfully added
        flash(Markup("Thanks \
                    <span class='message-helper bold italic'>" + user.capitalize() + "</span>, \
                    this recipe has been successfully edited!"))
        
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
    user = session['user'].lower()
    # Remove the recipe ID from that particular users' added_recipes list
    users_coll.find_one_and_update(
        {"username": user},
        {"$pull": {"added_recipes": ObjectId(recipe_id)}})
    # Remove the recipe ID from all users' liked_recipes list
    users_coll.update_many(
        {},
        {"$pull": {"liked_recipes": ObjectId(recipe_id)}})
    
    # Flash message confirmation that recipe has been successfully added
    flash(Markup("Thanks \
                <span class='message-helper bold italic'>" + user.capitalize() + "</span>, \
                this recipe has been successfully deleted!"))
    
    return redirect(url_for('get_recipes',
        page=1,
        recipe_id=recipe_id))

'''
RATE RECIPE
'''

@app.route('/rate/<recipe_id>', methods=["GET", "POST"])
def rate(recipe_id):
    '''
    Allows the user to rate the recipe
    Pushes the rating value into the rating_values list in the recipes collection
    '''
    username = session["user"]
    # Push rating from form into the rating_values field in the relevant record
    recipes_coll.update_one({"_id": ObjectId(recipe_id)},
        {"$push": {"rating_values": int(request.form.get("rating"))}})
    
    # Decrement number of views by 1
    # Resolves bug of it being incremented when redirected to recipes.html
    recipes_coll.update_one({"_id": ObjectId(recipe_id)},
        {"$inc": {"views": -1}})
    
    # Flash message confirmation that recipe has been successfully added
    flash(Markup("Thanks for rating this recipe \
                <span class='message-helper bold italic'>" + username.capitalize() + "</span>!"))
    
    return redirect(url_for('recipe',
            recipe_id=recipe_id))

'''
LIKE/UNLIKE RECIPE
'''

@app.route('/like_recipe/<recipe_id>')
def like_recipe(recipe_id):
    '''
    Allows the user to like a particular recipe
    The recipe_id is added to the user's liked_recipes list in the userLogin collection
    The 'likes' field in the recipes collection is incremented by 1
    The 'views' field in the recipes collection is decremented by 1
    '''
    
    # Add the liked recipe ID to the users collection for that user
    user = session['user'].lower()
    users_coll.find_one_and_update(
        {"username": user},
        {"$push": {"liked_recipes": ObjectId(recipe_id)}})
    
    # Increment 'likes' field in the recipes collection by 1 each time the recipe is liked
    recipes_coll.update_one(
        {"_id": ObjectId(recipe_id)},
        {"$inc": {"likes": 1, "views": -1}})
    
    # Flash message confirmation that the user successfully liked the recipe
    flash(Markup("Thanks \
                <span class='message-helper bold italic'>" + user.capitalize() + "</span>, \
                this recipe has been added to your 'Liked' list!"))
    
    return redirect(request.referrer)

@app.route('/unlike_recipe/<recipe_id>')
def unlike_recipe(recipe_id):
    '''
    Allows the user to unlike a particular recipe
    The recipe_id is removed from the user's liked_recipes list in the userLogin collection
    The 'likes' field in the recipes collection is decremented by 1
    The 'views' field in the recipes collection is decremented by 1 only if the recipe is unliked from recipe.html
    '''
    
    # Remove the liked recipe ID to the users collection for that user
    user = session['user'].lower()
    users_coll.find_one_and_update(
        {"username": user},
        {"$pull": {"liked_recipes": ObjectId(recipe_id)}})
    
    # Decrement 'likes' field in the recipes collection by 1 each time the recipe is liked
    recipes_coll.update_one(
        {"_id": ObjectId(recipe_id)},
        {"$inc": {"likes": -1}})
    
    # Only decrement views if the user unlikes a recipe on the recipe.html page
    # Resolves bug where views were decremented when the user unlikes a recipe in profile.html
    if request.path == 'recipe':
        recipes_coll.update_one(
            {"_id": ObjectId(recipe_id)},
            {"$inc": {"views": -1}})
    
    # Flash message confirmation that the user successfully liked the recipe
    flash(Markup("Thanks \
                <span class='message-helper bold italic'>" + user.capitalize() + "</span>, \
                this recipe has been removed from your 'Liked' list!"))
    
    return redirect(request.referrer)

'''
ERROR HANDLERS
'''
 # 404 error handler
@app.errorhandler(404)
def not_found_error(error):
    return render_template("errors/error_404.html"), 404

# 505 error handler
@app.errorhandler(500)
def something_wrong_error(error):
    return render_template("errors/error_500.html"), 500

# Catch all error handler
@app.route("/<path:path>")
def global_error(path):
    return render_template("errors/error_404.html"), 404

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=False)