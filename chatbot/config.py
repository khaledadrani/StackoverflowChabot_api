import os
from dotenv import load_dotenv

class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    MODEL_PATH = "./chatbot/"
    # SECRET_KEY = 'do-i-really-need-this'
    # FLASK_HTPASSWD_PATH = '/secret/.htpasswd'
    # FLASK_SECRET = SECRET_KEY
    #DB_HOST = 'database' # a docker link

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    MODEL_PATH = "app/chatbot"
    #DB_HOST = 'my.production.database' # not a docker link