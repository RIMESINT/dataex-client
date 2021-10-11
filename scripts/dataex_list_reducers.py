#!/usr/bin/env python3

"""List reducers CLI

This script allows the user to check the available reducer names for forecast analysis depending on the model type.

Usage:

$ dataex_list_reducers.py --model_type <str> --output_format <str> --output <str>

Options:

    model_type : str
                 ens or hres
   
    output_format : str
                    json, table or csv       

    output : str
             output filename

"""

import json
import pandas as pd
from dataexclient.auth import auth
from dataexclient.config import CHECK_REDUCERS_URL
import requests
from tabulate import tabulate
import click
from yaspin import yaspin



@click.command()
@click.option('--model_type', '-mt' ,required=True, type=click.Choice(['hres', 'ens'], case_sensitive=False))
@click.option('--output_format', '-of' ,required=False, default='table' ,type=click.Choice(['json','table' ,'csv'], case_sensitive=False))
@click.option('--output', '-o' ,required=False, help='output filename')


def main(model_type, output_format, output):

    payload = dict()
    payload['forecast_type'] = model_type
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
        response = requests.post(CHECK_REDUCERS_URL, headers=headers, data=json.dumps(payload))
        print(response.url)
        
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
                if output is not None:
                    if not output.endswith('.json'):
                        output += '.json'
                    with open(f'{output}', 'w') as f:
                        json.dump(data['reducers'], f)
                else:
                    print(data['reducers'])

            elif output_format in ['csv','table']:
                
                df = pd.DataFrame(data['reducers'])
                if output_format == 'table':
                    table = tabulate(df, headers='keys', showindex=False, tablefmt='psql')
                    if output is not None:
                        with open(output, 'w') as outfile:
                            outfile.write(table)
                    else:
                        print(table)
                
                elif output_format == 'csv':
                    if not output.endswith('.csv'):
                        output += '.csv'
                    df.to_csv(output, index=False)


        else:
            print(response.status_code)
            spinner.fail("💥 ")


if __name__=='__main__':
    main()




