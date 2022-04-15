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
import click
import requests

from yaspin import yaspin

from dataexclient import auth_helper
from dataexclient.config import GET_PARAMETER_INFO_URL
from dataexclient.utils import check_error, check_output_format


@click.command()
@click.option('--station_id', '-sid',required=False, help='Id number of station', type=click.STRING)
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
