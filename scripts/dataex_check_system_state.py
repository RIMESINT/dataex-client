#!/usr/bin/env python3


import json
import pandas as pd
from dataexclient import auth_helper
from dataexclient.config import CHECK_SYSTEM_STATE_URL
import requests
from tabulate import tabulate
import click
from yaspin import yaspin

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
        
        if response.status_code == 200:
            data = response.json()

            if 'error' in data:
                if data['error'] is None:
                    print(data['message'])    
                    spinner.text = "Done"
                    spinner.ok("✅")
                else:
                    print(data['error'],'-> ',data['message'])
                    spinner.fail("💥 ")

            if output is not None:
                if not output.endswith('.json'):
                    output += '.json'

                with open(f'{output}', 'w') as f:
                    json.dump(data['data'], f)
            else:
                print(data['data'])

        else:
            print(response.status_code)
            spinner.fail("💥 ")


if __name__=='__main__':
    main()


