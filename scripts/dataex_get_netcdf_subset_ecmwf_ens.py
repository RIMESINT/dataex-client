#!/usr/bin/env python3

"""Get NetCDF Subset ECMWF ENS CLI

This script allows the user to get a subset of ECMWF ENS data. 
This tool downloads the data in netCDF file format.

Usage:

$ get_netcdf_subset_ecmwf_ens.py -- params <str> --latbounds <float> <float> --lonbounds <float> <float> --out <str>

Options:
    params : str or list of str
             Single or comma seperated parameter short names
    latbounds : first float is for south and second float is for north
             South and North latitude values space seperated
    lonbounds : first float is for south and second float is for north
             West and East longitude values space seperated
    out : str
       output filename
"""

import json
import requests
import click
import sys
from yaspin import yaspin
from dataexclient.auth import auth
from dataexclient.config import GET_NETCDF_SUBSET_ENS_URL


parameters = [
    't2m_q5', 't2m_q25', 't2m_q50', 
    't2m_q75', 't2m_q95', 'lsp_q5',
    'lsp_q25', 'lsp_q50', 'lsp_q75', 
    'lsp_q95', 'cp_q5', 'cp_q25', 
    'cp_q50', 'cp_q75', 'cp_q95'
]

@click.command()
@click.option('--params', '-p', is_flag=False, default=','.join(parameters), show_default=True, metavar='<columns>', type=click.STRING, help='Select parameters')
@click.option('--latbounds', '-lat', required=True, nargs=2, type=float, help='Enter bottom lat and then top lat with space in between')
@click.option('--lonbounds', '-lon', required=True, nargs=2, type=float, help='Enter left lon and then right lon wuth space in between')
@click.option('--output', '-o', required=True, help='output filename')

def main(params, latbounds, lonbounds, output):



    params = [param.strip() for param in params.split(',')]
    payload = {}
    coords = {}
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

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(GET_NETCDF_SUBSET_ENS_URL, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:

            if response.headers['content-type'] == "application/json":
                data = response.json()
                print(data['error'], data['message'])
                spinner.fail("💥 ")
            else:
                spinner.text = "Done"
                spinner.ok("✅")
                if not output.endswith('.nc'):
                    output += '.nc' 
                with open(f'{output}', 'wb') as f:
                    f.write(response.content)

        else:
            print(response.status_code)
            spinner.fail("💥 ")
            
            


if __name__=='__main__':
    main()





