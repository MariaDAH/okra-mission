#################
#### imports ####
#################

from flask import render_template, request, flash, redirect, url_for
from okra import db
from . import geoservice_blueprint
from .forms import SearchForm
from okra.models import Ecobusiness


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
        result = Ecobusiness.query.filter_by(name=name).first_or_404()
        if result :
            flash('No results found for parameters, {}-{}-{}-{}!'.format(identifier,location, category, name))
        return redirect(url_for('geoservice.locationsmap',identifier=identifier, 
        location=location, category=category, name=name, result=result.name))
    return render_template('geoservice/searchbusiness.html', form=form)

@geoservice_blueprint.route('/locationsmap', methods=['GET', 'POST'])
def locationsmap():
    test = request.args['result']
    return render_template('geoservice/locationsmap.html', result=test)