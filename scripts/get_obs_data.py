"""Get Observation Data CLI

This script allows the user to get the specified observation data from Dataex server. 
This tool downloads the desired observation data in json format.

Usage:

$ get_obs_data.py --start_date <YYYY-MM-DD> --end_date <YYYY-MM-DD> -- stn_id <int> --p_id <int> --out <str>

Options:
    start_date : DateTime
                 Date in YYYY-MM-DD format
        
    end_date : DateTime
              Date in YYYY-MM-DD format
    stn_id : int
             station id
            
    p_id : int 
           parameter id     

    out : str
          output filename

"""


import json
import pandas as pd
import requests
import click
import json
import os
from yaspin import yaspin
from datetime import datetime as dt
import sys
from auth import auth
from CONFIG import GET_OBS_DATA_URL

@click.command()
@click.option('--start_date', required=True, help='Start date of obs data', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--end_date', required=True, help='End date of obs data ', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--stn_id', required=True, help='Id of desired station',type=int)
@click.option('--p_id', required=True, help='Id of desired parameter', type=int)
@click.option('--output_type', required=True, type=click.Choice(['json', 'csv'], case_sensitive=False))
@click.option('--out', required=True, help='output filename or path with filename')


def main(start_date, end_date, stn_id, p_id, output_type, out):
    
    if start_date > end_date:
        print("date range is invalid:start date is greater")
        return 0

    payload = {}
    payload['start_date'] = start_date.strftime('%Y-%m-%d')
    payload['end_date'] = end_date.strftime('%Y-%m-%d')
    payload['station_id'] = stn_id
    payload['param_id'] = p_id

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

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(GET_OBS_DATA_URL, headers=headers, data=json.dumps(payload))
        
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

            
            if output_type=='json':
                with open(f'{out}.json', 'w') as f:
                    json.dump(data, f)

            elif output_type=='csv':
                json_to_csv(data, out)

        else:
            print(response.status_code)
            spinner.fail("💥 ")




def json_to_csv(data, name):

    row = []
    values = []

    for obs in data['data']:
        row.append(obs['start_time'])
        row.append(obs['end_time'])
        row.append(obs['value'])
        values.append(row)
        row = []
    
    df = pd.DataFrame(values,columns=['start_time', 'end_time', 'value'])
    df.to_csv(f'{name}.csv', index=False)

 

if __name__=='__main__':
    main()




"""
payload = {
            'params': [ 'ssr', 't2m'],
            'domain': {
                    'left-lon': 100.0,   
                    'right-lon': 150.0,
                    'top-lat': 40.0,
                    'bottom-lat': 9.0
    }
}
"""
