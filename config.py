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
    SECRET_KEY='okra-secret'
    # Bcrypt algorithm hashing rounds
    BCRYPT_LOG_ROUNDS = 4


class ProductionConfig(Config):
    DEBUG = False
    DATABASE = 'production.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql:///' + os.path.join(BASEDIR, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ENV = 'development'
    DATABASE = 'staging.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql:///' + os.path.join(BASEDIR, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    ENV = 'development'
    DATABASE = 'development.db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql:///' + os.path.join(BASEDIR, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    TESTING = True
    DEBUG = False
    ENV = 'development'
    DATABASE = 'testing.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, DATABASE)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


