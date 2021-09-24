#!/usr/bin/env python3

"""Insert observation data CLI

This script allows the user to insert observation data into Dataex server. 
It can takes as input either csv or excel file containing the observations along with the country id number.

Usage:

$ insert_obs_data.py --country_id <int> --obs_data <str> 

Options:
    country_id : int
                 id number of country
    obs_data : str
               input filename either csv or excel   
"""

import sys
import json
import requests
import click
from yaspin import yaspin
import pandas as pd
from client.auth.auth import auth
from client.CONFIG import INSERT_OBS_DATA_URL


@click.command()
@click.option('--obs_data', required=True, help='filename or path to file with filename')
@click.option('--country_id', required=True ,type=int, help='id of country')

def main(obs_data, country_id):

    try:
        file = pd.read_csv(obs_data)
    except:
        file = pd.read_excel(obs_data, engine='openpyxl')

    payload = create_json(file, country_id)

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

    with yaspin(text="Inserting...", color="yellow") as spinner:

        response = requests.post(INSERT_OBS_DATA_URL, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            data = response.json()
            if data['error'] is None:
                print(data['message'])
                spinner.text = "Done"
                spinner.ok("✅")
            else:
                print(data['error'], data['message'])
                spinner.fail("💥 ")
            
        else:
            print(response.status_code)
            data = response.json()
            print(data['error'], data['message'])
            spinner.fail("💥 ")


def create_json(file, country_id):
    """Creates a json file
    
    Parameters
    ----------
    file : object
           dataframe
    country_id: str
                Id of country entered by the user
   
    Returns
    --------
    json 
          a json file containing rows of observation data
        
    """ 
    
    obs_data_json = {}
    data = []
    row = {}
    for i in range(len(file)):
        row['station_id'] = int(file.iloc[i]['station_id'])
        row['parameter_id'] = int(file.iloc[i]['parameter_id'])
        row['level_id'] = int(file.iloc[i]['level_id'])
        row['start_time'] = file.iloc[i]['start_time'] + 'Z'
        row['end_time'] = file.iloc[i]['end_time'] + 'Z'
        row['value'] = int(file.iloc[i]['value'])
        data.append(row)
        row = {}

    obs_data_json['country_id'] = country_id

    obs_data_json['data'] = data    

    return obs_data_json



if __name__=="__main__":
    main()


