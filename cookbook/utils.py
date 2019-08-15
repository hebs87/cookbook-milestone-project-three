from bson.objectid import ObjectId
from cookbook import mongo

# DB collection variables
recipes_coll = mongo.db.recipes
rating_coll = mongo.db.rating
categories_coll = mongo.db.categories
serves_coll = mongo.db.serves
time_coll = mongo.db.time
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
    These are arrays that are nested within categories object in the database
    Function uses key, val parameters to access the relevant nested array
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
