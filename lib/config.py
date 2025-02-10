#   Application configuration settings

# Import required modules
import os

class DefaultConfig(object):
    DEBUG = False
    TESTING = False
    SESSION_TYPE = None
    VITE_AUTO_INSERT = True
    SESSION_PERMANENT = False
    STATIC_FOLDER = "VueClient/src/assets"
    DATABASE_URL = os.getenv('DATABASE_URL')

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    TESTING = True
    SESSION_TYPE = "filesystem"
    DATABASE_URL = os.getenv('DATABASE_URL')

class ProdConfig(DefaultConfig):
    SESSION_TYPE = "filesystem"