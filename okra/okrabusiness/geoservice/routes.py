#################
#### imports ####
#################

from flask import render_template, request, flash, redirect, url_for

from . import geoservice_blueprint
from .forms import SearchForm
from okra.models import Business
from okra import db

################
#### routes ####
################
@geoservice_blueprint.route('/searchbusiness', methods=['GET', 'POST'])
def searchbusiness():

    form = SearchForm()
    if request.method == 'POST':
        identifier = form.identifier.data
        location = form.location.data
        category = form.category.data
        name = form.name.data
        return redirect(url_for('geoservice.locationsmap',identifier=identifier, 
        location=location, category=category, name=name))
    return render_template('geoservice/searchbusiness.html', form=form)

@geoservice_blueprint.route('/locationsmap', methods=['GET', 'POST'])
def locationsmap():
    return ''