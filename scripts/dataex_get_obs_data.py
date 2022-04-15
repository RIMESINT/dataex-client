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
import click
import requests

from yaspin import yaspin
from tabulate import tabulate

from dataexclient import auth_helper
from dataexclient.config import GET_OBS_DATA_URL
from dataexclient.utils import check_error, check_output_format

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
        print(response.url)
        
        if response.status_code == 200:
            data = response.json()
            if check_error(data):
                spinner.fail("💥 ")
            else:
                spinner.text = "Done"
                spinner.ok("✅")
                check_output_format(data['data'], output, output_format)
        else:
            print(response.status_code)
            spinner.fail("💥 ")

if __name__=='__main__':
    main()



