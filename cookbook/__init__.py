from flask import Flask
from flask_pymongo import PyMongo
from flask_uploads import UploadSet, configure_uploads, IMAGES
from cookbook.config import Config

# Instance of Flask
app = Flask(__name__)

# Config for storing uploaded images
images = UploadSet('images', IMAGES)

# Instance of PyMongo
mongo = PyMongo()

def create_app(config_class=Config):
    # Initialize and configure the instance of Flask
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Pass the app variable into othere variables
    mongo.init_app(app)
    configure_uploads(app, images)

    # Import routes
    from cookbook.errors.routes import errors
    from cookbook.main.routes import main
    from cookbook.recipes.routes import recipes
    from cookbook.users.routes import users
    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(recipes)
    app.register_blueprint(users)

    return app