import json
import requests
import click
import json
import os
from datetime import datetime as dt
import sys
sys.path.append('/home/anubinda/dataex-client/client/')
from auth import auth
from CONFIG import GET_OBS_DATA_URL

@click.command()
@click.option('--start_date', help='Start date of obs data', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--end_date', help='End date of obs data ', type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option('--stn_id', help='Id of desired station',type=int)
@click.option('--p_id', help='Id of desired parameter', type=int)
@click.option('--out', help='output filename or path with filename')

def main(start_date, end_date, stn_id, p_id, out):
    
    if start_date > end_date:
        print("date range is invalid:start should be before end")
        return 0

    payload = {}
    token = ''
    payload['start_date'] = start_date.strftime('%Y-%m-%d')
    payload['end_date'] = end_date.strftime('%Y-%m-%d')
    payload['station_id'] = stn_id
    payload['param_id'] = p_id

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


    response = requests.post(GET_OBS_DATA_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print(response.content)
    else:
        print(response.status_code)

    print(response.headers) 
    print(response.text)
    
    with open(f'{out}.json', 'w') as f:
        f.write(response.text)


if __name__=='__main__':
    main()




"""
payload = {
            'params': [ 'ssr', 't2m'],
            'domain': {
                    'left-lon': 100.0,   
                    'right-lon': 150.0,
                    'top-lat': 40.0,
                    'bottom-lat': 9.0
    }
}
"""
