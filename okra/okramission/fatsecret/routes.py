import os, json, csv
from flask import current_app as app
from flask import (
    flash, g, redirect, render_template, request, session, url_for, jsonify, json, session
)
from . import auth
from . import fatsecretapi as api
from . import fatsecret_blueprint
from flask_login import login_required
import flask


@fatsecret_blueprint.route('/searchfoods', methods=('GET', 'POST'))
@login_required
def searchfoods():

    if not session.get('oauth_token') is None:
        token = session['oauth_token']
    else:
        token = auth.authorization()
        session['oauth_token'] = token

    if request.method == 'POST':
        food = request.form["food"]  
        token = session['oauth_token']['access_token']
        client = api.Fatsecretapi(token)       
        foods = client.foods_search(food)

        dumped = json.dumps(foods)
        f = open("dict.json","w")
        f.write(dumped)
        f.close()

        test = json.loads(dumped)
        list = test['foods']
        list1 = list['food']

        return render_template('fatsecret/foodslist.html', foods=list1)

    return render_template('fatsecret/searchfoods.html')

@login_required
def select_item(id):
    url_for('getfood',id=id)


@fatsecret_blueprint.route('/getfood/<int:id>', methods=['GET'])
@login_required
def getfood(id):
    
    if request.method == 'POST':
        token = session['oauth_token']
        client = api.Fatsecretapi(token) 
        result = client.food_get(id)

    return render_template('fatsecret/foodetails.html')


