import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Update later by using a random number generator and moving
# the actual key outside of the source code under version control
class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    WTF_CSRF_ENABLED = False
    FLASK_APP = "okra" 
    #To be randomly generated
    SECRET_KEY='okra-secret' 
    # Bcrypt algorithm hashing rounds
    BCRYPT_LOG_ROUNDS = 4
    FATSECRET_TOKEN_ENDPOINT = 'https://oauth.fatsecret.com/connect/token'
    FATSECRET_REFRESH_ENDPOINT = 'https://oauth.fatsecret.com/connect/token'
    CLIENT_ID='40ca6a9cd34648fd80be50827fe46f7d'
    CLIENT_SECRET='27622b8b211f4ace9d57283a0cb06f89'
    MAIL_USERNAME='maria.herrero@okra.online'
    MAIL_PASSWORD=''
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class ProductionConfig(Config):
    DEBUG = False
    DATABASE = 'production.db'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, DATABASE)
    #SQLALCHEMY_TRACK_MODIFICATIONS = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ENV = 'development'
    DATABASE = 'staging.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ENV = 'development'
    DATABASE = 'development.db'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, DATABASE)
    #SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = False
    ENV = 'development'
    DATABASE = 'testing.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


