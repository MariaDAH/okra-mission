from flask import Blueprint
fatsecret_blueprint = Blueprint('fatsecret', __name__, template_folder='templates')

from . import routes
