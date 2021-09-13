import json
import requests
import click
import json
import os
from yaspin import yaspin
from datetime import datetime as dt
import sys
import pandas as pd
from auth import auth
from CONFIG import INSERT_OBS_DATA_URL


@click.command()
@click.option('--obs_data', help='json filename or path to json with filename')
@click.option('--country_id', type=int, help='json filename or path to json with filename')


def main(obs_data, country_id):

    try:
        file = pd.read_csv(obs_data)
    except:
        file = pd.read_excel(obs_data,engine='openpyxl')

    payload = create_json(file, country_id)

    #with open(obs_data, 'r') as f:
    #    data = json.load(f)

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

    with yaspin(text="Inserting", color="yellow") as spinner:

        response = requests.post(INSERT_OBS_DATA_URL, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            data = json.loads(response.text)
            if data['error'] is None:
                print(data['message'])
                spinner.ok("✅")
            else:
                print(data['error'], data['message'])
                spinner.fail("💥 ")
            
        else:
            print(response.status_code)
            data = json.loads(response.text)
            print(data['error'], data['message'])
            spinner.fail("💥 ")


def create_json(file, country_id):
    
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
        row={}

    obs_data_json['country_id'] = country_id

    obs_data_json['data'] = data    

    return obs_data_json

if __name__=="__main__":
    main()



'''
Json format for inserting data
Not allowing insertion of data from multiple countries at once

{   
    country_id : <int>,
    data: [
        { 
            station_id: <int>, 
            parameter_id: <int>, 
            level_id: <int>, 
            start_time: <date>, 
            end_time: <date>, 
            value: <float>
        },
        .
        .
        .
    ]
}
'''