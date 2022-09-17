#!/usr/bin/env python3

"""Get region data analysis CLI

This script allows the user to download analysis of hres/ens region data.

Usage:

$ dataex_region_data_analysis.py --model_type <str> --reducer <str> --asset_identifier <str> --unique_field <str> --output_format <str> --output <str>

Options:

    model_type : str
                 ens or hres(default)

    reducer : str
              name of reducer to use

    asset_identifier : str
                       identifier for asset

    unique_field : str
                   unique fields in asset

    output_format : str
                    json or xlsx

    output : str
             output filename

"""
import json
import click
import requests

from yaspin import yaspin

from dataexclient import auth_helper
from dataexclient.utils import check_error, check_output_format
from dataexclient.config import (
    GET_ECMWF_HRES_REGION_DATA_URL,
    GET_ECMWF_ENS_REGION_DATA_URL
)


@click.command()
@click.option(
    '--model_type',
    '-mt',
    required=True,
    type=click.Choice(
        [
            'ecmwf_hres', 'ecmwf_ens'
        ],
        case_sensitive=False
    )
)
@click.option(
    '--reducer',
    '-r',
    required=True,
    help='name of reducer',
    type=click.STRING
)
@click.option(
    '--asset_identifier',
    '-ai',
    required=True,
    help='unique identifier for asset',
    type=click.STRING
)
@click.option(
    '--unique_field',
    '-uf',
    required=True,
    help='unique fields in asset',
    type=click.STRING
)
@click.option(
    '--output_format',
    '-of',
    required=True,
    type=click.Choice(
        [
            'json', 'xlsx'
        ],
        case_sensitive=False
    )
)
@click.option(
    '--output',
    '-o',
    required=True,
    help='output filename'
)
def main(
    model_type,
    reducer,
    asset_identifier,
    unique_field,
    output_format,
    output
):
    if model_type == 'ecmwf_ens':
        URL = GET_ECMWF_ENS_REGION_DATA_URL
    elif model_type == 'ecmwf_hres':
        URL = GET_ECMWF_HRES_REGION_DATA_URL

    payload = dict()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }

    payload['reducer'] = reducer
    payload['asset_identifier'] = asset_identifier
    payload['unique_field'] = unique_field

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(
            URL,
            headers=headers,
            data=json.dumps(payload)
        )
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


if __name__ == '__main__':
    main()
