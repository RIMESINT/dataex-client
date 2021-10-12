#!/usr/bin/env python3

"""List User Forecast assets CLI

This script allows the user to get forecast asset information.

Usage:

$ dataex_list_user_assets.py 

"""

import json
import pandas as pd
from dataexclient.auth import auth
from dataexclient.config import GET_USER_ASSETS_URL
import requests
from tabulate import tabulate
import click
from yaspin import yaspin



def main():
    
    payload = dict()
    auth_obj = auth()
    try:
        is_token_valid = auth_obj.check_token()
    except:
        is_token_valid = False   
    
    if not is_token_valid:
        token = auth_obj.get_new_token_from_dataex()
    else:
        token = auth_obj.get_token()
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }

    cred = auth_obj.get_auth()
    payload['username'] = cred['username']

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(GET_USER_ASSETS_URL, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:

            data = response.json()

            if 'error' in data: 
                if data['error'] is None:
                    print(data['message'])    
                    spinner.text = "Done"
                    spinner.ok("✅")
                else:
                    print(data['error'],'-> ',data['message'])
                    spinner.fail("💥 ")


                df = pd.DataFrame(data['user_assets'])
                table = tabulate(df, headers='keys', showindex=False, tablefmt='psql')

                print(table)
 
        else:
            print(response.status_code)
            spinner.fail("💥 ")


if __name__=='__main__':
    main()



