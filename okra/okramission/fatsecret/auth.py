import functools, os, requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from werkzeug.security import check_password_hash, generate_password_hash
from flask import (
    flash, g, render_template, request, session, url_for, jsonify, redirect, json
)
from flask import current_app as app
from . import routes

#clientID = os.environ['CLIENT_ID']
#clientSecret = os.environ['CLIENT_SECRET']
clientID='40ca6a9cd34648fd80be50827fe46f7d'
clientSecret='27622b8b211f4ace9d57283a0cb06f89'

#token_endpoint = app.config['FATSECRET_TOKEN_ENDPOINT']

def authorization():
    '''Implement OAuth2 authorization to que access_token as a backend client'''
    url = 'https://oauth.fatsecret.com/connect/token'
    client = BackendApplicationClient(client_id=clientID)
    client.grant_type = 'client_credentials'
    oauth = OAuth2Session(client=client, scope='basic')
    token = oauth.fetch_token(token_url=url, client_id=clientID, client_secret=clientSecret)
    session['oauth_token'] = token
    return token

def refreshtoken():
    '''Implement OAuth2 authorization to que access_token as a backend client'''
    token = session['oauth_token']
    refresh_url = 'https://oauth.fatsecret.com/connect/token'
    def token_saver(token):
        session['oauth_token'] = token   
    extra = {
        'client_id': clientID,
        'client_secret': clientSecret,
    }
    client = OAuth2Session(clientID, token=token, auto_refresh_url=refresh_url,
        auto_refresh_kwargs=extra, token_updater=token_saver)
    jsonify(client.get(refresh_url).json())

    return jsonify(session['oauth_token'])

    
