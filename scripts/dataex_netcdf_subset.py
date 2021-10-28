#!/usr/bin/env python3

"""Get NetCDF Subset HRES/ENS/SEAS CLI

This script allows the user to get a subset of ECMWF HRES/ENS/SEAS data. 
This tool downloads the data in netCDF file format.

Usage:

$ dataex_netcdf_subset.py --model_type <str> --ens_params <str> --latbounds <float> <float> --lonbounds <float> <float> --output <str>

Options:
    model_type : str
                 type of model - ens or hres
        
    ens_params : str or list of str
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
from yaspin import yaspin
from dataexclient import auth_helper
from dataexclient.config import GET_NETCDF_SUBSET_URL, GET_NETCDF_SUBSET_ENS_URL


hres_parameters = [
    'u10', 'swvl1','swvl2', 'swvl3', 'swvl4', 
    'd2m', 'v10', 't2m', 'cp', 'lsp',
    'ssr', 'str', 'sshf', 'slhf'
]

ens_parameters = [
    't2m_q5', 't2m_q25', 't2m_q50', 
    't2m_q75', 't2m_q95', 'lsp_q5',
    'lsp_q25', 'lsp_q50', 'lsp_q75', 
    'lsp_q95', 'cp_q5', 'cp_q25', 
    'cp_q50', 'cp_q75', 'cp_q95'
]

@click.command()
@click.option('--model_type', '-mt' ,required=True, type=click.Choice(['hres', 'ens'], case_sensitive=False))
@click.option('--hres_params', '-hp', required=False, is_flag=False, metavar='<columns>', type=click.STRING, help='Select hres parameters')
@click.option('--ens_params', '-ep', required=False, is_flag=False, metavar='<columns>', type=click.STRING, help='Select ens parameters')
@click.option('--latbounds', '-lat', required=True, nargs=2, type=float, help='Enter bottom lat and then top lat with space in between')
@click.option('--lonbounds', '-lon', required=True, nargs=2, type=float, help='Enter left lon and then right lon with space in between')
@click.option('--output', '-o', required=True, help='output filename')

def main(model_type, hres_params, ens_params, latbounds, lonbounds, output):

    params = []

    if model_type == 'hres':
        URL = GET_NETCDF_SUBSET_URL
        if hres_params is None:
            params = hres_parameters
        else:
            params = [param.strip() for param in hres_params.split(',')]

    elif model_type == 'ens':
        URL = GET_NETCDF_SUBSET_ENS_URL
        if ens_params is None:
            params = ens_parameters
        else:
            params = [param.strip() for param in ens_params.split(',')]

    
    payload = {}
    coords = {}
    param_list = []
    for param in params:
        param_list.append(param)
    
    coords['bottom-lat'], coords['top-lat'], = latbounds
    coords['left-lon'],coords['right-lon'] = lonbounds
    payload['params'] = param_list
    payload['domain'] = coords
     
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(URL, headers=headers, data=json.dumps(payload))
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

