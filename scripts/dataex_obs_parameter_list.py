#!/usr/bin/env python3

"""Get Parameter Info CLI

This script allows the user to get station's parameter information such as ID number and name from Dataex server. 
This tool can download in either csv or json file.

Usage:

$ dataex_obs_parameter_list.py --station_id <int> --output_type <str> --output <str>

Options:

    station_id : int
              station id     

    output_type : str
                  json, table or csv       

    output : str
          output filename

"""

import json
import pandas as pd
from dataexclient import auth_helper
from dataexclient.config import GET_PARAMETER_INFO_URL
import requests
from tabulate import tabulate
import click
from yaspin import yaspin



@click.command()
@click.option('--station_id', '-sid',required=True, help='Id number of station', type=click.STRING)
@click.option('--output_format', '-of',required=False, default='table',type=click.Choice(['json', 'table' ,'csv'], case_sensitive=False))
@click.option('--output', '-o',required=False, help='output filename')


def main(station_id, output_format, output):
    
    payload = dict()
    payload['station_id'] = station_id
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.get(GET_PARAMETER_INFO_URL, headers=headers, params=payload)
        
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

                    if not output.endswith('.json'):
                        output += '.json'

                    with open(f'{output}', 'w') as f:
                        json.dump(data['data'], f)

                else:
                    print(data['data'])        

            elif output_format in ['csv','table']:

                df = pd.DataFrame( data['data'] )

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
