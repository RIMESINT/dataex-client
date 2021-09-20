
"""Fetch observation data summary CLI

This script allows the user to fetch summary of observation data statistics from Dataex server. 

Usage:

$ fetch_obs_summary.py \--out <str>

Options:
    out : str
          name of output file            

"""


import sys
import json
import requests
import click
import pandas as pd
from yaspin import yaspin
from auth import auth
from CONFIG import FETCH_OBS_SUMMARY_URL


@click.command()
@click.option('--out', required=True, help='output filename')
@click.option('--output_type', required=True, type=click.Choice(['json', 'csv'], case_sensitive=False))



def main(out, output_type):

    auth_obj = auth()
    try:
        is_token_valid = auth_obj.check_token()
    except:
        is_token_valid = False
    if not is_token_valid:
        token = auth_obj.get_new_token_from_dataex()
    else:
        token = auth_obj.get_token()

    headers = {
        'Content-Type': 'application/json',
        'Authorization': token
    }

    with yaspin(text="Fetching...", color="yellow") as spinner:

        response = requests.post(FETCH_OBS_SUMMARY_URL, headers=headers)
        data = response.json()
        if response.status_code == 200:

            if 'error' in data:
                if data['error'] is None:
                    print(data['message'])
                    spinner.text = "Done"
                    spinner.ok("✅")
                else:
                    print(data['message'])
                    spinner.fail("💥 ")

            if output_type=='json':
                with open(f'{out}.json', 'w') as f:
                    json.dump(data, f)
            elif output_type=='csv':
                json_to_csv(data, out)

        else:
            print(response.status_code)
            spinner.fail("💥 ")



          
def json_to_csv(data, name):

    row = []
    values = []

    for obs in data['summary']:
        row.append(obs['name'])
        row.append(obs['stn_num'])
        row.append(obs['time_period'])
        row.append(obs['total'])
        row.append(obs['miss_ptg'])
        values.append(row)
        row = []
    df = pd.DataFrame(values,columns=['name', 'stn_num', 'miss_ptg', 'total', 'time_period'])
    df.to_csv(f'{name}.csv', index=False)



if __name__=="__main__":
    main()
