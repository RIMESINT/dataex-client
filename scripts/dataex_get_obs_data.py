#!/usr/bin/env python3

"""Get Observation Data CLI

This script allows the user to get the specified observation data from Dataex server. 
This tool downloads the desired observation data in the selected format.

Usage:

$ dataex_get_obs_data.py --start_date <YYYY-MM-DD> --end_date <YYYY-MM-DD> -- station_id <int> --parameter_id <int> --output_type <str> --output <str>

Options:
    start_date : DateTime
                 Date in YYYY-MM-DD format
        
    end_date : DateTime
               Date in YYYY-MM-DD format
    
    station_id : int
                 station id
            
    parameter_id : int 
                   parameter id     

    output_type : str
                  json or csv       

    output : str
             output filename

"""

import json
import pandas as pd
from dataexclient import auth_helper
from dataexclient.config import GET_OBS_DATA_URL
import requests
from tabulate import tabulate
import click
from yaspin import yaspin



@click.command()
@click.option('--start_date','-sd',required=True, help='Start date of obs data', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--end_date', '-ed', required=True, help='End date of obs data ', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--station_id', '-si', required=True, help='Id of desired station',type=int)
@click.option('--parameter_id', '-pi', required=True, help='Id of desired parameter', type=int)
@click.option('--output_format', '-of', required=False, default='table' , help='output file format',type=click.Choice(['json','table','csv'], case_sensitive=False))
@click.option('--output', '-o', required=False, default=None, help='output filename')


def main(start_date, end_date, station_id, parameter_id, output_format, output):
    
    if start_date > end_date:
        print("date range is invalid:start date is greater")
        return 0

    payload = {}
    payload['start_date'] = start_date.strftime('%Y-%m-%d')
    payload['end_date'] = end_date.strftime('%Y-%m-%d')
    payload['station_id'] = station_id
    payload['param_id'] = parameter_id

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
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

            
            if output_format == 'json':
                if output is not None:
                    if not output.endswith('.json'):
                        output += '.json'

                    with open(f'{output}', 'w') as f:
                        json.dump(data['data'], f)
                else:
                    print(data['data'])
    
            elif output_format in ['csv','table']:

                df = pd.DataFrame(data['data'])

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



