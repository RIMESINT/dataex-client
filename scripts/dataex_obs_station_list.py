#!/usr/bin/env python3

"""Get Station Info CLI

This script allows the user to get country's station information such as ID number and name from Dataex server.
This tool can download in either csv or json file.

Usage:

$ dataex_get_station_list.py --country_id <int> --not_empty --output_format <str> --output <str>

Options:

    country_id : int
                 country id

    not_empty : include in command in order to only get some stations with data

    empty : include in command to get any station even if they are empty

    output_type : str
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
from dataexclient.config import GET_STATION_INFO_URL
from dataexclient.utils import check_error, check_output_format


@click.command()
@click.option(
    '--country_id',
    '-cid',
    required=True,
    help='Id number of country',
    type=click.STRING
)
@click.option(
    '--not_empty/--empty',
    required=False,
    help='Option to choose either stations that are empty or not',
    default=False
)
@click.option(
    '--output_format',
    '-of',
    required=False,
    default='table',
    type=click.Choice(
        [
            'json', 'table', 'csv'
        ],
        case_sensitive=False
    )
)
@click.option(
    '--output',
    '-o',
    required=False,
    help='output filename'
)
def main(
    country_id,
    not_empty,
    output_format,
    output
):
    payload = dict()
    payload['country_id'] = country_id

    if not_empty:
        payload['not_empty'] = True
    else:
        payload['not_empty'] = None

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(
            GET_STATION_INFO_URL,
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
