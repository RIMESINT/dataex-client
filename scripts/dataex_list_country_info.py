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
                  json, table or csv       

    output : str
          output filename

"""

import json
import click
import requests

import pandas as pd

from yaspin import yaspin
from tabulate import tabulate

from dataexclient import auth_helper
from dataexclient.config import GET_COUNTRY_INFO_URL
from dataexclient.utils import check_error, check_output_format



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

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(GET_COUNTRY_INFO_URL, headers=headers, data=json.dumps(payload))
        print(response.url)
        
        if response.status_code == 200:
            data = response.json()
            if check_error(data):
                spinner.fail("💥 ")
            else:
                spinner.text = "Done"
                spinner.ok("✅")
            check_output_format(data['info'], output, output_format)
        else:
            print(response.status_code)
            spinner.fail("💥 ")


if __name__=='__main__':
    main()