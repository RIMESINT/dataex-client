#!/usr/bin/env python3

"""List reducers CLI

This script allows the user to check the available reducer names for performing forecast analysis depending on the model type.

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
import click
import requests

from yaspin import yaspin
from tabulate import tabulate

from dataexclient import auth_helper
from dataexclient.config import CHECK_REDUCERS_URL
from dataexclient.utils import check_error, check_output_format


@click.command()
@click.option(
    '--model_type', '-mt',
    required=True,
    type=click.Choice(
        [
            'ecmwf_hres', 'ecmwf_ens'
        ],
        case_sensitive=False)
)
@click.option(
    '--output_format', '-of',
    required=False, default='table',
    type=click.Choice(
        [
            'json', 'table', 'csv'
        ],
        case_sensitive=False)
)
@click.option(
    '--output', '-o',
    required=False,
    help='output filename'
)
def main(model_type, output_format, output):

    payload = dict()
    payload['forecast_type'] = model_type

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(
            CHECK_REDUCERS_URL,
            headers=headers,
            data=json.dumps(payload)
        )
        print(response.url)

        if response.status_code == 200:
            data = response.json()
            if check_error(data):
                spinner.fail("💥 ")
            else:
                spinner.text = "Done"
                spinner.ok("✅")
                check_output_format(data['reducers'], output, output_format)
        else:
            print(response.status_code)
            spinner.fail("💥 ")


if __name__ == '__main__':
    main()
