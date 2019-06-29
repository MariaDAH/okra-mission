from flask import Blueprint
okramission_blueprint = Blueprint('okramission', __name__, template_folder='templates')

from . import fatsecret
from . import dashboards
