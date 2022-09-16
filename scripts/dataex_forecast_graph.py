#!/usr/bin/env python3
"""CLI to get forecast graph"""
import json
import click
import requests

from yaspin import yaspin

from dataexclient import auth_helper
from dataexclient.config import (
    GET_HRES_GRAPH_URL, GET_ENS_GRAPH_URL, GET_SEAS_GRAPH_URL
)
from dataexclient.utils import export_graph, is_response_okay


@click.command()
@click.option(
    '--model_type',
    '-mt',
    required=True,
    type=click.Choice(
        [
            'ecmwf_hres', 'ecmwf_ens', 'ecmwf_seas'
        ],
        case_sensitive=False
    )
)
@click.option(
    '--ecmwf_hres_param',
    '-hp',
    required=False,
    help='Type one ecmwf hres parameter name'
)
@click.option(
    '--ecmwf_ens_param',
    '-ep',
    required=False,
    help='Type one ecmwf ens parameter name'
)
@click.option(
    '--ecmwf_seas_param',
    '-sp',
    required=False,
    help='Type one ecmwf seas parameter name'
)
@click.option(
    '--quantile',
    '-q',
    required=False,
    type=click.Choice(
        [
            'q5', 'q25', 'q50', 'q75', 'q95'
        ],
        case_sensitive=False
    ),
    help='Choose a quantile with ECMWF ENS parameters'
)
@click.option(
    '--day',
    '-d',
    required=False,
    type=click.Choice(
        [
            '1', '2', '3', '4', '5',
            '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15'
        ],
        case_sensitive=False
    ),
    help=('Choose the day of forecast you want'
          'of either ecmwf ens or ecmwf hres')
)
@click.option(
    '--month',
    '-m',
    required=False,
    type=click.Choice(
        [
            '1', '2', '3',
            '4', '5', '6', '7'
        ],
        case_sensitive=False
    ),
    help='Choose the month of forecast you want of ecmwf seas'
)
@click.option(
    '--latbounds',
    '-lat',
    required=True,
    nargs=2,
    type=float,
    help=('Enter bottom lat and then'
          'top lat with space in between')
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
def main(
    model_type,
    ecmwf_hres_param,
    ecmwf_ens_param,
    ecmwf_seas_param,
    quantile,
    day,
    month,
    latbounds,
    lonbounds,
    output
):

    payload = {}
    coords = {}
    param = ''

    with yaspin(text="Initializing...", color="yellow") as spinner:
        if model_type == 'ecmwf_hres':
            URL = GET_HRES_GRAPH_URL
            if day is None:
                spinner.text = "please choose a forecast day"
                spinner.fail("💥 ")
                return

            if int(day) > 10:
                spinner.text = "request failed...hres is 10 lead days only"
                spinner.fail("💥 ")
                return

            if quantile:
                print("Ignoring quantile parameter"
                      "as ECMWF HRES has no quantile data")

            if ecmwf_hres_param is None:
                print("Please provide a parameter from HRES")
                spinner.text = "request failed...select a parameter"
                spinner.fail("💥 ")
                return
            else:
                param = ecmwf_hres_param
                payload['indx'] = int(day) - 1

        elif model_type == 'ecmwf_ens':
            URL = GET_ENS_GRAPH_URL
            if day is None:
                spinner.text = "please choose a forecast day"
                spinner.fail("💥 ")
                return

            if quantile is None:
                print("Please select a quantile with parameter from ENS")
                spinner.text = "request failed...select a quantile"
                spinner.fail("💥 ")
                return
            else:
                payload['quantile'] = quantile

            if ecmwf_ens_param is None:
                print("Please provide a parameter from ENS")
                spinner.text = "request failed...select a parameter"
                spinner.fail("💥 ")
                return
            else:
                param = ecmwf_ens_param
                payload['indx'] = int(day) - 1

        elif model_type == 'ecmwf_seas':
            URL = GET_SEAS_GRAPH_URL
            if month is None:
                spinner.text = "please choose a forecast month"
                spinner.fail("💥 ")
                return

            if quantile is None:
                print("Please select a quantile with parameter from SEAS")
                spinner.text = "request failed...select a quantile"
                spinner.fail("💥 ")
                return
            else:
                payload['quantile'] = quantile

            if ecmwf_seas_param is None:
                print("Please provide a parameter from SEAS ENS")
                spinner.text = "request failed...select a parameter"
                spinner.fail("💥 ")
                return
            else:
                param = ecmwf_seas_param
                payload['indx'] = int(month) - 1

    coords['bottom-lat'], coords['top-lat'] = latbounds
    coords['left-lon'], coords['right-lon'] = lonbounds
    payload['param'] = param
    payload['domain'] = coords

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token(),
    }

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(
            URL,
            stream=True,
            headers=headers,
            data=json.dumps(payload)
        )
        if response.status_code == 200:
            init_time = response.headers['init_time']
            if is_response_okay(response):
                export_graph(response.content, output)
                spinner.text = (f"Downloaded...Init time of "
                                f"forecast is {init_time}")
                spinner.ok("✅")
            else:
                spinner.fail("💥 ")

        else:
            print(response.status_code)
            spinner.fail("💥 ")


if __name__ == '__main__':
    main()
