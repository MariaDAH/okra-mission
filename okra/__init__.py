import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask import render_template

#######################
#### Configuration ####
#######################

# Create the instances of the Flask extensions (flask-sqlalchemy, flask-login, etc.) in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.
db = SQLAlchemy()
bcrypt = Bcrypt()
login = LoginManager()
login.login_view = "users.login"


######################################
#### Application Factory Function ####
######################################

def create_app(config_filename=None):

    #using config file
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(config_filename)

    #using setup from environment variable and config file
    #app = Flask(__name__, instance_path=os.path.abspath(os.path.dirname(__file__)))
    #app.config.from_object(os.environ['APP_SETTINGS'])
    
    initialize_extensions(app)
    register_blueprints(app)
    
    @app.route('/home')
    def home():
        return render_template('home.html')

    app.add_url_rule('/', 'home', home)
    
    return app


##########################
#### Helper Functions ####
##########################

def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    db.init_app(app)
    bcrypt.init_app(app)
    login.init_app(app)

    # Flask-Login configuration
    from okra.models import User
    from okra.models import Business

    with app.app_context():
        db.create_all()

    @login.user_loader
    def load_user(user_id):
        return User.query.filter(User.id == int(user_id)).first()


def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from okra.users import users_blueprint
    from okra.okrabusiness import okrabusiness_blueprint
    from okra.okrabusiness.geoservice import geoservice_blueprint
    from okra.okramission import okramission_blueprint
    from okra.okramission.dashboards import dashboards_blueprint
    from okra.okramission.fatsecret import fatsecret_blueprint
    app.register_blueprint(users_blueprint)
    app.register_blueprint(okrabusiness_blueprint)
    app.register_blueprint(geoservice_blueprint)
    app.register_blueprint(okramission_blueprint)
    app.register_blueprint(dashboards_blueprint)
    app.register_blueprint(fatsecret_blueprint)

