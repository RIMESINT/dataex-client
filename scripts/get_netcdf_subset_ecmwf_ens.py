"""Get NetCDF Subset ECMWF ENS CLI

This script allows the user to get a subset of ECMWF ENS data. 
This tool downloads the data in netCDF file format.

Usage:

$ get_netcdf_subset_ecmwf_ens.py \-- params <str> \--latbounds <float> <float> \--lonbounds <float> <float> \--out <str>

Options:
    params : str or list of str
             Single or comma seperated parameter short names \n
    latbounds : first float is for south and second float is for north
             South and North latitude values space seperated \n
    lonbounds : first float is for south and second float is for north
             West and East latitude values space seperated \n 
    out : str
       output filename
    
        

"""

import json
import time
import requests
import click
from io import BytesIO 
import getpass
import json
import os
import sys
from yaspin import yaspin
from auth import auth
from CONFIG import GET_NETCDF_SUBSET_ENS_URL


parameters = [
    't2m_q5', 't2m_q25', 't2m_q50', 
    't2m_q75', 't2m_q95', 'lsp_q5',
    'lsp_q25', 'lsp_q50', 'lsp_q75', 
    'lsp_q95', 'cp_q5', 'cp_q25', 
    'cp_q50', 'cp_q75', 'cp_q95'
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

    with yaspin(text="Downloading", color="yellow") as spinner:
        response = requests.post(GET_NETCDF_SUBSET_ENS_URL, headers=headers, data=json.dumps(payload))
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
