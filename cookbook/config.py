import os


# Create Config class and move environmental variables into it
class Config:
    UPLOADED_IMAGES_DEST = "cookbook/static/img"
    MONGO_DBNAME = 'onlineCookbook'
    MONGO_URI = os.getenv('MONGO_URI')
    SECRET_KEY = os.urandom(24)
