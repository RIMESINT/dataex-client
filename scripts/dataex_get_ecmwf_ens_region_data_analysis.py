#!/usr/bin/env python3

"""Get ecmwf ens region data CLI

This script allows the user to download analysis of ecmwf ens region data analysis.

Usage:

$ dataex_get_ecmwf_ens_region_data_analysis.py --reducer <str> --asset_identifier <str> --unique_field <str> --output_format <str> --out <str>

Options:
   
    reducer : str
              name of reducer to use

    asset_identifier : str
                       identifier for asset
    
    unique_field : str
                   unique fields in asset

    output_format : str
                  json or xlsx     

    out : str
          output filename

"""

import sys
import json
import pandas as pd
from dataexclient.auth import auth
from dataexclient.config import GET_ECMWF_ENS_REGION_DATA_URL
import requests
import click
from yaspin import yaspin


@click.command()
@click.option('--reducer', '-r', required=True, help='name of reducer', type=click.STRING)
@click.option('--asset_identifier', '-ai', required=True, help='unique identifier for asset', type=click.STRING)
@click.option('--unique_field', '-uf', required=True, help='unique fields in asset', type=click.STRING)
@click.option('--output_format', '-of' , required=True, type=click.Choice(['json', 'xlsx'], case_sensitive=False))
@click.option('--output', '-o' , required=True, help='output filename')


def main(reducer, asset_identifier, unique_field, output_format, output):
    

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

    payload['reducer'] = reducer
    payload['asset_identifier'] = asset_identifier
    payload['unique_field'] = unique_field

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(GET_ECMWF_ENS_REGION_DATA_URL, headers=headers, data=json.dumps(payload))
        
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

                if not output.endswith('.json'):
                    output += '.json'

                with open(f'{output}', 'w') as f:
                    json.dump(data['data'], f)

            elif output_format=='xlsx':
                json_to_excel(data['r_data'], output)

        else:
            print(response.status_code)
            spinner.fail("💥 ")



def json_to_excel(data, name):
    
    writer = pd.ExcelWriter(name)
    start_dates = []
    end_dates = []
    _values= []

    for key, val in data.items():
        for inner_key, inner_val in val.items():
            
            if inner_key=='time':
                for dates in inner_val:
                    start_dates.append(dates[0])
                    end_dates.append(dates[1])
                    
            
            if inner_key=='value':
                for value in inner_val:
                    _values.append(value)
        
            
        df_start_dates = pd.DataFrame(start_dates, columns=['start_date'])
        df_end_dates = pd.DataFrame(end_dates, columns=['end_date'])
        df_values = pd.DataFrame(_values, columns=['values'])
        df = pd.concat([df_start_dates, df_end_dates, df_values],axis=1)
        df.to_excel(writer, sheet_name=key, index=False)
        _values = []
        start_dates = []
        end_dates = []
    
    writer.close()



if __name__=='__main__':
    main()



