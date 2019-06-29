from flask import request
import functools, os, requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import requests
import base64
import json

class Fatsecretapi:

    uri = "https://platform.fatsecret.com/rest/server.api"

    def __init__(self, token):
        self.access_token = token
    
    def gettoken(self):
        return self.access_token

    def foods_search(self,search_expression, page_number=None, max_results=None):

        payload={'method': 'foods.search', 'search_expression':search_expression, 'format':'json'} 
      
        headers = {
            'ContenType':'application/json',
            #'Authorization':'%s' % "%s%s" % ('Bearer'.encode('utf-8'), base64.b64encode(self.access_token.encode('utf-8'))) 
            'Authorization':'Bearer %s' % self.access_token
        }
   
        if page_number!=None:
            payload['page_number'] = page_number
        if max_results!=None:
            payload['max_results'] = max_results
      
        response = requests.request('POST', self.uri, headers=headers, params=payload)
        
        return response.json()
   
    def food_get(self,food_id):
        """Returns nutrition information and the corresponding fatsecret information URL for the specified food_id
        food_ids may be obtained by using foods_search()"""

        if food_id is None:
            return None

        headers = {
            'ContenType':'application/json',
            #'Authorization':'%s' % "%s%s" % ('Bearer'.encode('utf-8'), base64.b64encode(self.access_token.encode('utf-8'))) 
            'Authorization':'Bearer %s' % self.access_token  
        }

        payload={'method': 'food.get','food_id':food_id,'format':'json'} 

        response=requests.request('GET', self.uri, headers=headers, params=payload)
    
        return response.content
