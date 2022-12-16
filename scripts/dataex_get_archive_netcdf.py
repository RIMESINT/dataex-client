#!/usr/bin/env python3

"""Get NetCDF Subset ECMWF HRES/ENS/SEAS CLI

This script allows the user to download a subset of ECMWF HRES/ENS/SEAS data which has been
archived by user provided date.

Usage:

$ dataex_get_archive_netcdf_subset.py --model_type <str> --ens_params <str> --latbounds <float> <float> --lonbounds <float> <float> --output <str> --date <str>

"""

import json
import click
import requests

from yaspin import yaspin

from dataexclient import auth_helper
from dataexclient.utils import export_nc, is_response_okay

from dataexclient.config import GET_ARCHIVE_NETCDF_URL

ecmwf_hres_parameters = [
    'u10', 'swvl1', 'swvl2', 'swvl3', 'swvl4',
    'd2m', 'v10', 't2m', 'cp', 'lsp',
    'ssr', 'sshf'
]

ecmwf_seas_parameters = ecmwf_ens_parameters = [
    't2m_q5', 't2m_q25', 't2m_q50',
    't2m_q75', 't2m_q95', 'lsp_q5',
    'lsp_q25', 'lsp_q50', 'lsp_q75',
    'lsp_q95', 'cp_q5', 'cp_q25',
    'cp_q50', 'cp_q75', 'cp_q95'
]

@click.command()
@click.option(
    '--model_type',
    '-mt',
    required=True,
    type=click.Choice(
        [
            'ecmwf_hres', 'ecmwf_ens', 'ecmwf_seas'
        ],
        case_sensitive=False)
)
@click.option(
    '--ecmwf_hres_params',
    '-hp',
    required=False,
    is_flag=False,
    metavar='<columns>',
    type=click.STRING,
    help='Select ecmwf hres parameters'
)
@click.option(
    '--ecmwf_ens_params',
    '-ep',
    required=False,
    is_flag=False,
    metavar='<columns>',
    type=click.STRING,
    help='Select ecmwf ens parameters'
)
@click.option(
    '--ecmwf_seas_params',
    '-sp',
    required=False,
    is_flag=False,
    metavar='<columns>',
    type=click.STRING,
    help='Select ecmwf seas parameters'
)
@click.option(
    '--latbounds',
    '-lat',
    required=True,
    nargs=2,
    type=float,
    help='Enter bottom lat and then top lat with space in between'
)
@click.option(
    '--lonbounds',
    '-lon',
    required=True,
    nargs=2,
    type=float,
    help='Enter left lon and then right lon with space in between'
)
@click.option(
    '--output',
    '-o',
    required=True,
    help='output filename'
)

@click.option(
    '--date',
    '-d',
    required=True,
    help='Date of archived netcdf',
    type=click.DateTime(formats=["%Y%m%d"])
)
def main(
    model_type,
    ecmwf_hres_params,
    ecmwf_ens_params,
    ecmwf_seas_params,
    latbounds,
    lonbounds,
    output,
    date
):
    params = []
    URL = GET_ARCHIVE_NETCDF_URL

    if model_type == 'ecmwf_hres':
        if ecmwf_hres_params is None:
            params = ecmwf_hres_parameters
        else:
            params = [param.strip() for param in ecmwf_hres_params.split(',')]
    elif model_type == 'ecmwf_ens':
        if ecmwf_ens_params is None:
            params = ecmwf_ens_parameters
        else:
            params = [param.strip() for param in ecmwf_ens_params.split(',')]
    elif model_type == 'ecmwf_seas':
        if ecmwf_seas_params is None:
            params = ecmwf_ens_parameters
        else:
            params = [param.strip() for param in ecmwf_seas_params.split(',')]

    payload = {}
    coords = {}
    param_list = []
    for param in params:
        param_list.append(param)

    coords['bottom-lat'], coords['top-lat'], = latbounds
    coords['left-lon'], coords['right-lon'] = lonbounds
    payload['params'] = param_list
    payload['domain'] = coords
    payload['date'] = date.strftime('%Y%m%d')
    payload['model_type'] = model_type

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token(),
    }

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(
            URL,
            headers=headers,
            data=json.dumps(payload)
        )
        if response.status_code == 200:
            if is_response_okay(response):
                init_time = response.headers['init_time']
                export_nc(response.content, output)
                spinner.text = (f"Downloaded...Init time "
                                f"of forecast is {init_time}")
                spinner.ok("✅")
            else:
                spinner.fail("💥 ")

        else:
            print(response.status_code)
            print(response.content)
            spinner.fail("💥 ")


if __name__ == '__main__':
    main()
