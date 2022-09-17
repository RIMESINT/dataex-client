#!/usr/bin/env python3

import json
import click
import requests

from yaspin import yaspin

from dataexclient.auth import auth
from dataexclient import auth_helper
from dataexclient.utils import check_error

from dataexclient.config import (SET_REGION_DEFAULT_URL,
                                 SET_POINT_DEFAULT_URL)


@click.command()
@click.option(
    '--preference_type',
    '-pt',
    required=True,
    help='choose either region or point',
    type=click.Choice(
        [
            'region', 'point'
        ],
        case_sensitive=False
    )
)
@click.option(
    '--preference_identifier',
    '-pi',
    required=True,
    help='unique identifier for preference',
    type=click.STRING
)
def main(
    preference_type,
    preference_identifier
):
    payload = dict()
    auth_obj = auth()
    cred = auth_obj.get_auth()
    payload['username'] = cred['username']
    if preference_type == 'region':
        url = SET_REGION_DEFAULT_URL
        payload['region_id'] = preference_identifier
    else:
        url = SET_POINT_DEFAULT_URL
        payload['point_id'] = preference_identifier

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
                if 'is_default' in data:
                    print('It is already a default!')
                spinner.text = "Done"
                spinner.ok("✅")

        else:
            print(response.status_code)
            spinner.fail("💥 ")


if __name__ == '__main__':
    main()
