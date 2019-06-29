from flask import Blueprint
geoservice_blueprint = Blueprint('geoservice', __name__, template_folder='templates')

from . import routes
