#!/usr/bin/env python3

"""Fetch observation data summary

This script allows the user to fetch summary of observation data statistics from Dataex. 

Usage:

$ dataex_obs_data_summary.py --output <str> --output-format <str>

Options:
    output: str
            name of output file 

    output-format: str
                   json, table or csv      

"""


import json
import requests
import click
import pandas as pd
from yaspin import yaspin
from tabulate import tabulate
from dataexclient.auth import auth
from dataexclient.config import FETCH_OBS_SUMMARY_URL


@click.command()
@click.option(
    '--output', '-o',
    required=False,
    default=None,
    help = 'output filename'
)
@click.option(
    '--output_format', '-of', 
    required=False,
    type=click.Choice(['json', 'table', 'csv'], case_sensitive=False),
    default='table',
    help= 'output file format'
)
def main(output,output_format):

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

    with yaspin(text="Fetching...", color="yellow") as spinner:

        response = requests.post(FETCH_OBS_SUMMARY_URL, headers=headers)
        data = response.json()
        
        if response.status_code == 200:

            if 'error' in data:
                if data['error'] is None:
                    spinner.text = "Data fetched successfully"
                    spinner.ok("✅")
                else:
                    print(data['message'])
                    spinner.fail("💥 ")

            if output_format == 'json':
                
                if output is not None:
                    with open(output,'w') as outfile:
                        json.dump(data['countries'], outfile)
                else:
                    print(data['countries'])
            
            elif output_format in ['table','csv']:

                df = pd.DataFrame( data['countries'] )
                
                if output_format == 'table':
                    table = tabulate(df, headers='keys', showindex=False, tablefmt='psql')

                    if output is not None: 

                        with open(output, 'w') as outfile:
                            outfile.write(table)
                        
                    else:
                        print(table)
                
                elif output_format == 'csv':

                    csv = df.to_csv( output, index=False)

        else:
            print(response.status_code)
            spinner.fail("💥 ")
        

if __name__=="__main__":
    main()