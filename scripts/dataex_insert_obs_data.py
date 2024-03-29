#!/usr/bin/env python3

"""Insert observation data CLI

This script allows the user to insert observation data into Dataex server.
It can takes as input either csv or excel file containing the observations along with the country id number.

Usage:

$ dataex_insert_obs_data.py --country_id <int> --obs_data <str>

Options:
    country_id : int
                 id number of country

    obs_data : str
               input csv or excel file
"""

import json
import click
import requests

import pandas as pd
from yaspin import yaspin

from dataexclient import auth_helper
from dataexclient.config import INSERT_OBS_DATA_URL
from dataexclient.utils import check_error, create_json


@click.command()
@click.option(
    '--obs_data',
    '-obs',
    required=True,
    help='filename or path to file with filename'
)
@click.option(
    '--country_id',
    '-cid',
    required=True,
    type=int,
    help='id of country'
)
def main(obs_data, country_id):

    try:
        file = pd.read_csv(obs_data)
    except:
        file = pd.read_excel(obs_data, engine='openpyxl')

    payload = create_json(file, country_id)

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }

    with yaspin(text="Inserting...", color="yellow") as spinner:

        response = requests.post(
            INSERT_OBS_DATA_URL,
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
        else:
            print(response.status_code)
            data = response.json()
            print(data['error'], data['message'])
            spinner.fail("💥 ")


if __name__ == "__main__":
    main()
