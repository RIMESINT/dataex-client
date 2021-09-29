#!/usr/bin/env python3

"""Get NetCDF Subset ECMWF HRES CLI

This script allows the user to get a subset of ECMWF HRES data. 
This tool downloads the data in netCDF file format.

Usage:

$ get_netcdf_subset_ecmwf_hres.py -- params <str> --latbounds <float> <float> --lonbounds <float> <float> --out <str>

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
from dataexclient.config import GET_NETCDF_SUBSET_URL


parameters = [
    'u10', 'swvl1','swvl2', 'swvl3', 'swvl4' 
    'd2m', 'v10', 't2m', 'cp', 'lsp'
    'ssr', 'str', 'sshf', 'slhf'

]

@click.command()
@click.option('--params', '-p', is_flag=False, default=','.join(parameters), show_default=True, metavar='<columns>', type=click.STRING, help='Select parameters')
@click.option('--latbounds', '-lat', required=True, nargs=2, type=float, help='Enter bottom lat and then top lat with space in between')
@click.option('--lonbounds', '-lon', required=True, nargs=2, type=float, help='Enter left lon and then right lon with space in between')
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
        response = requests.post(GET_NETCDF_SUBSET_URL, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:

            if response.headers['content-type'] == "application/json":
                data = response.json()
                print(data['error'], data['message'])
                spinner.fail("💥 ")
            else:
                if not output.endswith('.nc'):
                    output += '.nc'

                with open(f'{output}', 'wb') as f:
                    f.write(response.content)
                spinner.text = "Done"    
                spinner.ok("✅")

        else:
            print(response.status_code)
            spinner.fail("💥 ")
           


if __name__=='__main__':
    main()

