#!/usr/bin/env python3

"""List User Forecast assets CLI

This script allows the user to get forecast asset information.

Usage:

$ dataex_list_user_assets.py 

"""

import json
import requests

from yaspin import yaspin
from tabulate import tabulate

from dataexclient.auth import auth
from dataexclient import auth_helper
from dataexclient.config import GET_USER_ASSETS_URL
from dataexclient.utils import check_error, check_output_format



def main():
    
    payload = dict()
    auth_obj = auth()
    cred = auth_obj.get_auth()
    payload['username'] = cred['username']

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(GET_USER_ASSETS_URL, headers=headers, data=json.dumps(payload))
        print(response.url)
        
        if response.status_code == 200:
            data = response.json()
            if check_error(data):
                spinner.fail("💥 ")
            else:
                spinner.text = "Done"
                spinner.ok("✅")
                check_output_format(data['user_assets'], output_format='table')
        else:
            print(response.status_code)
            spinner.fail("💥 ")

if __name__=='__main__':
    main()



