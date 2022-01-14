#!/usr/bin/env python3

import os
import json
import requests
import click
import pandas as pd
from yaspin import yaspin
from tabulate import tabulate
from dataexclient.auth import auth
from dataexclient import auth_helper
from dataexclient.config import GET_FCST_GRAPH_PARAMS_URL


@click.command()
@click.option(
    '--model_type', '-mt' ,
    required=True, 
    type=click.Choice(['hres', 'ens'], case_sensitive=False), 
    help='choose model type'
)

def main(model_type):
    
    payload = dict()       
    payload['model_type'] = model_type
        
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(GET_FCST_GRAPH_PARAMS_URL, headers=headers, data=json.dumps(payload))

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

                df = pd.DataFrame( data['params'] )
                table = tabulate(df, headers='keys', showindex=False, tablefmt='psql')
                print(table)

        else:
            print(response.status_code)
            spinner.fail("💥 ")

if __name__=='__main__':
    main()

