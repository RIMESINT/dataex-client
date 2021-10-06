#!/usr/bin/env python3

"""List Country Info CLI

This script allows the user to get country information such as ID number from Dataex server. 
This tool can download in either csv or json file.

Usage:

$ dataex_list_country_info.py --country <str> --output_format <str> --output <str>

Options:

    country : str
              name of country      

    output_format : str
                  json or csv       

    output : str
          output filename

"""

import json
import pandas as pd
from dataexclient.auth import auth
from dataexclient.config import GET_COUNTRY_INFO_URL
import requests
import click
from yaspin import yaspin
from tabulate import tabulate



@click.command()
@click.option(
    '--country', '-c', 
    type=click.STRING,
    help='optional - either give country name or just leave it from command line', 
)
@click.option(
    '--output_format', '-of', 
    required=False, 
    default='table',
    type=click.Choice(['json', 'csv', 'table'], case_sensitive=False)
)
@click.option(
    '--output', '-o',
    required=False, 
    help='output filename or path with filename'
)


def main(country, output_format, output):
    

    payload = dict()

    if country is None:
        payload['country'] = None
    else:
        payload['country'] = country.lower()

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

            if output_format == 'json':

                if output is not None:

                    if output.endswith('.json'):

                        with open(f'{output}', 'w') as f:
                            json.dump(data['info'], f)

                else:
                    print(data['info'])

            elif output_format in ['table','csv']:

                df = pd.DataFrame(data['info'])

                if output_format == 'table':

                    table = tabulate(df, headers='keys', showindex=False, tablefmt='psql')
                    
                    if output is not None:

                        with open(output, 'w') as outfile:
                            outfile.write(table)

                    else:
                        print(table)

                elif output_format == 'csv':

                    if output is not None:

                        if not output.endswith('.csv'):
                            output += '.csv'

                        df.to_csv(output, index=False)


        else:
            print(response.status_code)
            spinner.fail("💥 ")




if __name__=='__main__':
    main()



