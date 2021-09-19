
import os
import getpass
import json
from sys import path
import requests
import jwt
import CONFIG
from datetime import datetime as dt, timedelta as delt


class auth():

    home_dir = os.environ['HOME']

    def __init__(self):

        path_to_file = os.path.join(self.home_dir, '.dataex_auth.json')
        data = {}
        if not os.path.exists(path_to_file):
            data = self.create_auth()
        else:    
            with open(f'{self.home_dir}/.dataex_auth.json', 'r') as f:
                data = json.load(f)

        self.auth = data



    def get_auth(self):
        data = {}
        path_to_file = os.path.join(self.home_dir, '.dataex_auth.json')
        if not os.path.exists(path_to_file):
            return self.create_auth()
        else:
            with open(f'{self.home_dir}/.dataex_auth.json', 'r') as f:
                 data = json.load(f)
        
        self.auth = data
        return self.auth


    def check_token(self):

        print("checking token...")
        data =  self.auth
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': data['token']
        }
        response = requests.post(CONFIG.CHECK_TOKEN_URL, headers=headers)
        
        res_dict  = json.loads(response.text)
        
        if res_dict['error'] is None:
            print(res_dict['message'])
            return True

        print(res_dict['error'], "-> ", res_dict['message'])
        return False
    
      
        
    def create_auth(self):
        username = input("Enter your dataex username:")
        password = getpass.getpass(prompt="Enter your password:")
        auth_json = {}
        auth_json['username'] = username
        auth_json['password'] = password
        auth_json['token'] = ''

        with open(f'{self.home_dir}/.dataex_auth.json','w') as f:
            json.dump(auth_json, f)

        return auth_json



    def get_token(self):

        return self.get_token_local_fs()


    def get_token_local_fs(self):

        data = dict()        
        path_to_file = os.path.join(self.home_dir, '.dataex_auth.json')

        if not os.path.exists(path_to_file):
            data = self.create_auth()
        else:
            data = self.auth

        if data['token'] == '':
            
            data['token'] = self.get_new_token_from_dataex()


        return data['token']

        

    def get_new_token_from_dataex(self):
        
        print("getting new token...")
        data = dict()
        data['username'] = self.auth['username']
        data['password'] = self.auth['password']
        token_response = requests.post(CONFIG.GET_TOKEN_URL, data=data)
        response_dict = token_response.json()
        if response_dict['error'] is None:
            print(response_dict['message'])
            self.auth['token'] = response_dict['token']    
            with open(f'{self.home_dir}/.dataex_auth.json','w') as f:
                    json.dump(self.auth, f)


        try:
            return response_dict['token']
        except:
            print(response_dict['message'])
  