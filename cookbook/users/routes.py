import re
from flask import (
    Blueprint, render_template, redirect, request,
    session, url_for, flash, Markup)
from bson.objectid import ObjectId
from werkzeug.security import check_password_hash, generate_password_hash
from cookbook.utils import recipes_coll, users_coll, get_username

# Blueprint instance to users route
users = Blueprint("users", __name__)


'''
USER LOGIN AND LOGOUT FUNCTIONALITY
'''


@users.route('/login_register')
def login_register():
    return render_template("login_register.html")


@users.route('/login', methods=["GET", "POST"])
def login():
    '''
    Login
    Checks that the user exists, and that user's password matches the
    hashed password in the database
    '''
    if request.method == "POST":

        username = request.form.get('username').lower()
        password = request.form.get("password")
        existing_user = get_username(username)

        # Check username exists and password matches hashed password
        if existing_user and check_password_hash(
                                                existing_user["password"],
                                                password):
            flash(Markup("Welcome back \
                        <span class='message-helper bold italic'>" +
                         username.capitalize() +
                         "</span>, you're now logged in!"))
            session["user"] = username
            return redirect(url_for('main.index', username=session["user"]))
        # If username OR password don't match, display generic flash message
        else:
            flash(Markup("It appears those details don't match what we have,\
            please try again."))
            return redirect(url_for('users.login'))

    return render_template("login_register.html")


@users.route('/register', methods=["GET", "POST"])
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

        # Check username is alphanumeric
        for letter in new_username:
            if not letter.isalnum():
                flash(Markup("Usernames must be alphanumeric only. \
                                Please try another one."))
                return redirect(url_for('users.register'))

        # Check username and password are between 6-15 characters
        # Not visible, as min/ max length set in the HTML input fields
        if len(new_username) < 5 or len(new_username) > 15:
            flash(Markup("Usernames must be between 5 and 15 characters. \
                            Please try again."))
            return redirect(url_for('users.register'))

        if len(new_password) < 5 or len(new_password) > 15:
            flash(Markup("Passwords must be between 5 and 15 characters. \
                            Please try again."))
            return redirect(url_for('users.register'))

        # Check if username already exists
        existing_user = get_username(new_username)
        if existing_user:
            flash(Markup("Sorry, \
                        <span class='message-helper bold italic'>" +
                         new_username.capitalize() + "</span> \
                         is already taken! Please choose another one."))
            return redirect(url_for('users.register'))

        # If all checks pass, add user to the database and hash the password
        users_coll.insert_one({
            "username": new_username,
            "password": generate_password_hash(new_password),
            "added_recipes": [],
            "liked_recipes": []
        })
        session["user"] = new_username
        flash(Markup("Thanks for signing up \
                    <span class='message-helper bold italic'>" +
                     new_username.capitalize() + "</span>, \
                     you're now logged in!"))

        return redirect(url_for('main.index', username=session["user"]))

    return render_template("login_register.html")


@users.route('/logout')
def logout():
    '''
    Remove the session cookie and end the user session
    '''
    session.pop('user', None)
    flash(Markup("You were successfully logged out. Come back soon!"))

    return redirect(url_for('main.index'))


'''
USER'S PROFILE PAGE
'''


@users.route('/profile/<username>', methods=["GET", "POST"])
def profile(username):
    '''
    Loads the content on the user's profile page
    Gets the user's added and liked recipes
    '''
    username = get_username(session["user"])["username"]

    # Get all recipes from the recipes_coll that were added by the user's ID
    user_id = get_username(session["user"])["_id"]
    user_added_list = recipes_coll.find({'$and': [{"added_by": user_id},
                                        {"deleted": False}]})\
                                  .sort([('name', 1)])

    # Get all recipes that the user has liked
    liked_recipes = get_username(session["user"])["liked_recipes"]
    user_liked_list = recipes_coll.find({"_id": {"$in": liked_recipes}})\
                                  .sort([("name", 1)])

    return render_template(
                        "profile.html",
                        username=username,
                        user_added_list=user_added_list,
                        user_liked_list=user_liked_list
                        )


'''
CHANGE PASSWORD
'''


@users.route('/profile/<username>/change_password', methods=["POST"])
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
                    <span class='message-helper bold italic'>" +
                     user.capitalize() + "</span>, \
                     your password has successfully been changed!"))
        users_coll.update_one(
            {"username": user},
            {"$set": {"password": generate_password_hash(changed_password)}})
    # If stored password doesn't match the entry, display generic flash message
    else:
        flash(Markup("Sorry \
                    <span class='message-helper bold italic'>" +
                     user.capitalize() + "</span>, \
                     your existing password doesn't match what we have! \
                     Please try again."))

    return redirect(url_for('users.profile', username=username))


'''
DELETE ACCOUNT
'''


@users.route('/profile/<username>/delete_account', methods=["POST"])
def delete_account(username):
    '''
    Allows the user to delete their account
    Users will have to enter their correct existing password first
    Deleting the account will delete the user's recipes
    'Deleted' value will be updated to true and they won't be displayed
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
        user_added_recipes = [recipe for recipe in username
                              .get("added_recipes")]
        # Update 'deleted' value to true for each recipe from recipes_coll
        # Remove each recipe from all other users' liked list
        for recipe in user_added_recipes:
            recipes_coll.update_one({"_id": ObjectId(recipe)},
                                    {"$set": {"deleted": True}})
            users_coll.update_many(
                {},
                {"$pull": {"liked_recipes": ObjectId(recipe)}})
        # Find the user's liked recipes
        user_liked_recipes = [recipe for recipe in username
                              .get("liked_recipes")]
        # Decrement the likes field in each of those recipes by 1
        for recipe in user_liked_recipes:
            recipes_coll.update_one({"_id": ObjectId(recipe)},
                                    {"$inc": {"likes": -1}})
        flash(Markup("Your account has been successfully deleted."))
        # End the user's session
        session.pop('user', None)
        # Remove the user's details from the userLogin collection
        users_coll.remove({"_id": username.get("_id")})
        # Redirect to index.html
        return redirect(url_for('main.index'))
    # If stored password doesn't match the entry, display generic flash message
    else:
        flash(Markup("Sorry \
                    <span class='message-helper bold italic'>" +
                     user_upper + "</span>, \
                     your existing password doesn't match what we have. \
                     Please try again."))

    return redirect(url_for('users.profile', username=username))
