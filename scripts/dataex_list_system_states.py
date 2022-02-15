#!/usr/bin/env python3
'''CLI to list Dataex system states'''
import json
import requests

from yaspin import yaspin
from tabulate import tabulate

from dataexclient import auth_helper
from dataexclient.config import LIST_SYSTEM_STATES_URL
from dataexclient.utils import check_error, check_output_format


def main():
    payload = dict()

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(LIST_SYSTEM_STATES_URL, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            data = response.json()
            if check_error(data):
                spinner.fail("💥 ")
            else:
                spinner.text = "Done"
                spinner.ok("✅")
            check_output_format(data['system_states'], output_format='table')
        else:
            print(response.status_code)
            spinner.fail("💥 ")

if __name__=='__main__':
    main()


