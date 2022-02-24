#!/usr/bin/env python3
"""CLI to get available parameters for forecast graphs and animation"""
import json
import click
import requests

from yaspin import yaspin

from dataexclient import auth_helper
from dataexclient.config import GET_FCST_GRAPH_PARAMS_URL
from dataexclient.utils import check_error, check_output_format


@click.command()
@click.option(
    '--model_type', '-mt' ,
    required=True, 
    type=click.Choice(['ecmwf_hres', 'ecmwf_ens', 'ecmwf_seas'], case_sensitive=False), 
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
            if check_error(data):
                spinner.fail("💥 ")
            else:
                spinner.text = "Done"
                spinner.ok("✅")
            check_output_format(data['params'], output_format='table')
        else:
            print(response.status_code)
            spinner.fail("💥 ")


if __name__=='__main__':
    main()
