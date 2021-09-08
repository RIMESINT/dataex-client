import json
import requests
import click
import json
import os
from datetime import datetime as dt
import sys
sys.path.append('/home/anubinda/dataex-client/client/')
from auth import auth
from CONFIG import INSERT_OBS_DATA_URL


@click.command()
@click.option('--obs_data', help='path to file with filename')

def main(obs_data):

    with open(obs_data, 'r') as f:
        data = json.load(f)

    auth_obj = auth()
    
    try:
        is_token_valid = auth_obj.check_token()
    except:
        is_token_valid = False    

    if is_token_valid:
        token = auth_obj.get_new_token_from_dataex()
    else:
        token = auth_obj.get_token()

    headers = {
        'Content-Type': 'application/json',
        'Authorization': data['token'] 
    }


    response = requests.post(INSERT_OBS_DATA_URL, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print(response.content)
    else:
        print(response.status_code)


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