#################
#### imports ####
#################

from flask import render_template, request, flash, redirect, url_for
from okra import db
from . import geoservice_blueprint
from .forms import SearchForm
from okra.models import Ecobusiness
from okra.models import Category


################
#### routes ####
################
@geoservice_blueprint.route('/searchbusiness', methods=['GET', 'POST'])
def searchbusiness():
    categories = Category.query.all()
    form = SearchForm()
    if request.method == 'POST':
        identifier = form.identifier.data
        location = form.location.data
        category_id = form.category_id.data
        name = form.name.data
        result = Ecobusiness.query.filter_by(name=name).first_or_404()
        if result :
            flash('No results found for parameters, {}-{}-{}-{}!'.format(identifier,location, category_id, name))
        return redirect(url_for('geoservice.locationsmap',identifier=identifier, 
        location=location, category=category_id, name=name, result=result.name))
    return render_template('geoservice/searchbusiness.html', form=form, categories=categories)

@geoservice_blueprint.route('/locationsmap', methods=['GET', 'POST'])
def locationsmap():
    name = request.args['result']
    return render_template('geoservice/locationsmap.html', name=name)