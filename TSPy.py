import os
import requests
import json
import datetime
import urllib
from dotenv import load_dotenv

load_dotenv()

class TSClient():

    def __init__(self, client_id:str, secret_key:str, username:str, redirect_uri:str, sim_environment:bool=True):
        self.client_id = client_id
        self.secret_key = secret_key
        self.username = username
        self.sim_environment = sim_environment
        self.redirect_uri = redirect_uri
        self.response_type = 'code'
        self.authorize_url = "https://api.tradestation.com/v2/authorize"
        self.sim_authorize_url = "https://sim-api.tradestation.com/v2/authorize"


        self.config = {
            'client_id': client_id,
            'secret_key': secret_key,
            'username': username,
            'sim_environment': sim_environment,
            'redirect_uri':'https://google.com',
        }
    
    def authenticate(self):

        if self.sim_environment:
            
            query_string = urllib.parse.urlencode({
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'response_type': self.response_type
            })
            
            access_url = '{}?{}'.format(self.sim_authorize_url, query_string)

            print(access_url)
            return access_url
            
        
        else:

            query_string = urllib.parse.urlencode({
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'response_type': self.response_type
            })  
            
            access_url = '{}?{}'.format(self.sim_authorize_url, query_string)

            print(access_url)           
            return access_url

    
API_KEY = os.getenv('API_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')
USERNAME = os.getenv('USERNAME')
PORT = 8080
REDIRECT_URI = 'http://localhost:{}'.format(PORT)


Object = TSClient(
                client_id = API_KEY, 
                secret_key = SECRET_KEY,
                username = USERNAME,
                redirect_uri = REDIRECT_URI,
                sim_environment = True
)

Object.authenticate()

    



