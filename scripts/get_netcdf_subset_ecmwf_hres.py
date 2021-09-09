import json
import requests
import click
from io import BytesIO 
import getpass
import json
import os
import sys
from yaspin import yaspin
from auth import auth
from CONFIG import GET_NETCDF_SUBSET_URL


parameters = [
    'u10', 'swvl1','swvl2', 'swvl3', 'swvl4' 
    'd2m', 'v10', 't2m', 'cp', 'lsp'
    'ssr', 'str', 'sshf', 'slhf'

]

@click.command()
@click.option('--params', is_flag=False, default=','.join(parameters), show_default=True, metavar='<columns>', type=click.STRING, help='Select parameters')
@click.option('--latbounds', nargs=2, type=float, help='Enter bottom lat and then top lat; seperate values with space')
@click.option('--lonbounds', nargs=2, type=float, help='Enter left lon and then right lon; sepearate values with space')
@click.option('--out', help='output filename or full path with filename')

def main(params, latbounds, lonbounds, out):

    params = [param.strip() for param in params.split(',')]
    payload = {}
    coords = {}
    token = ''

    param_list = []
    for par in params:
        param_list.append(par)
    
    coords['bottom-lat'], coords['top-lat'], = latbounds
    coords['left-lon'],coords['right-lon'] = lonbounds
    payload['params'] = param_list
    payload['domain'] = coords
    
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

    with yaspin(text="Success", color="yellow") as spinner:
        response = requests.post(GET_NETCDF_SUBSET_URL, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            spinner.ok("✅")
            if response.headers['content-type'] == "application/json":
                data = json.loads(response.text)
                print(data['error'], data['message'])
                spinner.fail("💥 ")
        else:
            print(response.status_code)
            spinner.fail("💥 ")
            
            

        with open(f'{out}.nc', 'wb') as f:
            f.write(response.content)
    
    
    
    
    

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
