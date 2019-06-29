#################
#### imports ####
#################

from flask import render_template, request, flash, redirect, url_for

from . import okrabusiness_blueprint
from .forms import RegisterForm
from okra.models import Business
from okra import db
import datetime

################
#### routes ####
################
@okrabusiness_blueprint.route('/registerbusiness', methods=['GET', 'POST'])
def registerbusiness():

    form = RegisterForm()
    registered_on = datetime.date.today
    updated_on = datetime.date.today
    if request.method == 'POST' and form.validate_on_submit():
        new_business = Business(form.name.data, form.userid.data, form.website.data, 
        form.location.data, form.category.data, form.telephonenumber.data, form.commnent.data, form.subscriptionplan.data,
        form.email.data, registered_on, updated_on)
        db.session.add(new_business)
        db.session.commit()
        flash('Thanks for registering, {}!'.format(new_business.email))
        return redirect(url_for('business.profile'))
    return render_template('okrabusiness/registerbusiness.html', form=form)