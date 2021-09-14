
"""Fetch observation data summary

This script allows the user to fetch summary of observation data statistics from Dataex server. 

Usage:

$ fetch_obs_summary.py 

Parameters
---------

out : str
    name of output file            

"""



import json
import requests
import click
import json
import os
from yaspin import yaspin
import sys
from auth import auth
from CONFIG import FETCH_OBS_SUMMARY_URL


@click.command()
@click.option('--out', help='output filename')



def main(out):

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

    with yaspin(text="Fetching", color="yellow") as spinner:

        response = requests.post(FETCH_OBS_SUMMARY_URL, headers=headers)

        if response.status_code == 200:
            data = json.loads(response.text)
            if data['error'] is None:
                print(data['message'])
                spinner.ok("✅")
            else:
                spinner.fail("💥 ")
            
        else:
            print(response.status_code)
            spinner.fail("💥 ")
            
        with open(f'{out}.json', 'w') as f:
            f.write(response.text)

          
    


if __name__=="__main__":
    main()
