#!/usr/bin/env python3

import json
import click
import requests

from yaspin import yaspin

from dataexclient.auth import auth
from dataexclient import auth_helper
from dataexclient.utils import check_error, check_output_format

from dataexclient.config import GET_REGION_PREFERENCE_URL, GET_POINT_PREFERENCE_URL

@click.command()
@click.option('--preference_type', '-pt' ,required=True, help='choose either region or point',type=click.Choice(['region', 'point'], case_sensitive=False))


def main(preference_type):
    payload = dict()
    auth_obj = auth()
    cred = auth_obj.get_auth()
    payload['username'] = cred['username']
    if preference_type == 'region':
        url = GET_REGION_PREFERENCE_URL
        type = 'regions'
    else:
        url = GET_POINT_PREFERENCE_URL
        type = 'points'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token(),
    }

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            data = response.json()
            if check_error(data):
                spinner.fail("💥 ")
            else:
                spinner.text = "Done"
                spinner.ok("✅")
                check_output_format(data[type], output_format='table')
        else:
            print(response.status_code)
            spinner.fail("💥 ")


if __name__=='__main__':
    main()
