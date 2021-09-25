#!/usr/bin/env python3

"""Get Country Info CLI

This script allows the user to get country information such as ID number and name from Dataex server. 
This tool can download in either csv or json file.

Usage:

$ dataex_get_country_info.py --country <str> --output_format <str> --out <str>

Options:

    country : str
              name of country      

    output_format : str
                  json or csv       

    out : str
          output filename

"""

import sys
import json
import pandas as pd
from dataex_client_core.auth import auth
from dataex_client_core.CONFIG import GET_COUNTRY_INFO_URL
import requests
import click
from yaspin import yaspin
from tabulate import tabulate



@click.command()
@click.option('--country', '-c', help='optional - either give country name or just leave it from command line', type=click.STRING)
@click.option('--output_format', '-of' ,required=True, type=click.Choice(['json', 'csv'], case_sensitive=False))
@click.option('--out', '-o' ,required=True, help='output filename or path with filename')


def main(country, output_format, out):
    

    payload = dict()

    if country is None:
        payload['country'] = country
    else:
        payload['country'] = country.lower()

    print(payload)
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
        response = requests.post(GET_COUNTRY_INFO_URL, headers=headers, data=json.dumps(payload))
        
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

            if output_format=='json':
                with open(f'{out}.json', 'w') as f:
                    json.dump(data['info'], f)
            elif output_format=='csv':
                json_to_csv(data, out)

        else:
            print(response.status_code)
            spinner.fail("💥 ")




def json_to_csv(data, name):

    row = []
    values = []

    for obs in data['info']:
        row.append(obs['id'])
        row.append(obs['name'])
        values.append(row)
        row = []
    
    df = pd.DataFrame(values,columns=['id', 'name'])
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
