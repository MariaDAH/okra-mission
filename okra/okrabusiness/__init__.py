from flask import Blueprint
okrabusiness_blueprint = Blueprint('okrabusiness', __name__, template_folder='templates')

from . import geoservice
from . import routes

