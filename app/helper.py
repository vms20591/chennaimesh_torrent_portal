from flask import current_app
from flask_pymongo import PyMongo

#Retrieve or Create Mongo object
#Added this so as to prevent the following error,
#"UserWarning: MongoClient opened before fork. Create MongoClient with connect=False, or create client after forking"
#https://github.com/MongoEngine/mongoengine/issues/1234
def get_db():
    if hasattr(current_app,'mongo'):
        return current_app.mongo.db
    else:
        current_app.mongo=PyMongo(current_app._get_current_object())
        return current_app.mongo.db

#Helper to check if a file is in allowed list
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in current_app.config.get('ALLOWED_EXTENSIONS',[])
