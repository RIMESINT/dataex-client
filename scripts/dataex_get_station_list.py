#!/usr/bin/env python3

"""Get Station Info CLI

This script allows the user to get country's station information such as ID number and name from Dataex server. 
This tool can download in either csv or json file.

Usage:

$ dataex_get_station_info.py --country_id <int> --output_type <str> --out <str>

Options:

    country : int
              country id     

    output_type : str
                  json or csv       

    out : str
          output filename

"""

import sys
import json
import pandas as pd
from client.auth.auth import auth
from client.CONFIG import GET_STATION_INFO_URL
import requests
import click
from yaspin import yaspin



@click.command()
@click.option('--country_id', required=True, help='Id number of country', type=click.STRING)
@click.option('--not_empty/--empty', help='Option to filter stations that are empty', default=False)
@click.option('--output_type', required=True, type=click.Choice(['json', 'csv'], case_sensitive=False))
@click.option('--out', required=True, help='output filename or path with filename')


def main(country_id, not_empty, output_type, out):
    

    payload = dict()
    payload['country_id'] = country_id

    if not_empty:
        payload['not_empty'] = True
    else:
        payload['not_empty'] = None

    
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
        response = requests.get(GET_STATION_INFO_URL, headers=headers, data=payload)
        
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
                    json.dump(data['data'], f)
            elif output_type=='csv':
                json_to_csv(data, out)

        else:
            print(response.status_code)
            spinner.fail("💥 ")


def json_to_csv(data, name):

    row = []
    values = []

    for obs in data['data']:
        row.append(obs['id'])
        row.append(obs['name'])
        row.append(obs['lat'])
        row.append(obs['lon'])
        row.append(obs['country__name'])
        row.append(obs['wmo_id'])
        row.append(obs['station_type'])
        row.append(obs['maintainer__name'])
        row.append(obs['maintainer__website'])
        values.append(row)
        row = []
    
    df = pd.DataFrame(values,columns=['id', 'name', 'lat', 'lon', 'country_name', 'wmo_id', 'station_type', 'maintainer__name', 'maintainer__website'])
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
