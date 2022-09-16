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
import click
import requests

from yaspin import yaspin
from tabulate import tabulate

from dataexclient import auth_helper
from dataexclient.config import FETCH_OBS_SUMMARY_URL
from dataexclient.utils import check_error, check_output_format


@click.command()
@click.option(
    '--output',
    '-o',
    required=False,
    default=None,
    help='output filename'
)
@click.option(
    '--output_format',
    '-of',
    required=False,
    type=click.Choice(
        [
            'json', 'table', 'csv'
        ],
        case_sensitive=False
    ),
    default='table',
    help='output file format'
)
def main(output, output_format):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }

    with yaspin(text="Fetching...", color="yellow") as spinner:
        response = requests.post(
            FETCH_OBS_SUMMARY_URL,
            headers=headers
        )
        data = response.json()
        print(response.url)

        if response.status_code == 200:
            data = response.json()
            if check_error(data):
                spinner.fail("💥 ")
            else:
                spinner.text = "Done"
                spinner.ok("✅")
                check_output_format(data['countries'], output, output_format)
        else:
            print(response.status_code)
            spinner.fail("💥 ")


if __name__ == "__main__":
    main()
