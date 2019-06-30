#################
#### imports ####
#################

from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required
from . import okrabusiness_blueprint
from .forms import RegisterForm
from okra.models import Ecobusiness
from okra import db
import datetime

################
#### routes ####
################
@okrabusiness_blueprint.route('/registerbusiness', methods=['GET', 'POST'])
@login_required
def registerbusiness():

    form = RegisterForm()
    registered_on = datetime.datetime.now()
    updated_on = datetime.datetime.now()
    if request.method == 'POST' and form.validate_on_submit():
        new_business = Ecobusiness(form.name.data, form.user_id.data, form.website.data, 
        form.location.data, form.category.data, form.phonenumber.data, form.comment.data, 
        form.subscriptionplan.data, form.email.data, registered_on, updated_on)
        db.session.add(new_business)
        db.session.commit()
        flash('Thanks for registering, {}!'.format(new_business.name))
        return redirect(url_for('okrabusiness.profilebusiness'))
    return render_template('okrabusiness/registerbusiness.html', form=form)

@okrabusiness_blueprint.route('/profilebusiness', methods=['GET'])
@login_required
def profilebusiness():
    return render_template('okrabusiness/profilebusiness.html')