#!/usr/bin/env python3
"""CLI to get dataex system states"""
import json
import click
import requests

from yaspin import yaspin
from tabulate import tabulate

from dataexclient import auth_helper
from dataexclient.config import CHECK_SYSTEM_STATE_URL
from dataexclient.utils import check_error, check_output_format

@click.command()
@click.option('--state_name', '-sn', required=True, help='name of system state',type=str)
@click.option('--output', '-o', required=False, default=None, help='output filename')


def main(state_name, output):
    payload = dict()

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }
    payload['state_name'] = state_name

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(CHECK_SYSTEM_STATE_URL, headers=headers, data=json.dumps(payload))
        print(response.url)

        if response.status_code == 200:
            data = response.json()
            if check_error(data):
                spinner.fail("💥 ")
            else:
                spinner.text = "Done"
                spinner.ok("✅")
            check_output_format(data['data'], output)
        else:
            print(response.status_code)
            spinner.fail("💥 ")

if __name__=='__main__':
    main()


