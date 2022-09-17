#!/usr/bin/env python3
"""CLI to get forecast video"""
import json
import click
import requests

from yaspin import yaspin

from dataexclient import auth_helper
from dataexclient.config import (GET_HRES_ANIMATED_GRAPH_URL,
                                 GET_ENS_ANIMATED_GRAPH_URL,
                                 GET_SEAS_ANIMATED_GRAPH_URL)
from dataexclient.utils import export_html_video, is_response_okay


@click.command()
@click.option('--model_type',
              '-mt', required=True,
              type=click.Choice(
                    [
                        'ecmwf_hres', 'ecmwf_ens', 'ecmwf_seas'
                    ],
                    case_sensitive=False))
@click.option('--ecmwf_hres_param', '-hp',
              required=False,
              help='Type one ecmwf hres parameter name')
@click.option('--ecmwf_ens_param', '-ep',
              required=False,
              help='Type one ecmwf ens parameter name')
@click.option('--ecmwf_seas_param', '-sp',
              required=False,
              help='Type one ecmwf seas parameter name')
@click.option('--quantile', '-q',
              required=False,
              type=click.Choice(
                    [
                        'q5', 'q25', 'q50', 'q75', 'q95'
                    ],
                    case_sensitive=False),
              help=(
                'Choose a quantile with ECMWF ENS or ECMWF SEAS parameters'
              ))
@click.option('--latbounds', '-lat',
              required=True, nargs=2, type=float,
              help='Enter bottom lat and then top lat with space in between')
@click.option('--lonbounds', '-lon',
              required=True, nargs=2, type=float,
              help='Enter left lon and then right lon with space in between')
@click.option('--output', '-o',
              required=True,
              help='output filename')
def main(
    model_type,
    ecmwf_hres_param,
    ecmwf_ens_param,
    ecmwf_seas_param,
    quantile,
    latbounds,
    lonbounds,
    output
):
    payload = {}
    coords = {}
    param = ''

    with yaspin(text="Initializing...", color="yellow") as spinner:
        if model_type == 'ecmwf_hres':
            URL = GET_HRES_ANIMATED_GRAPH_URL
            if quantile:
                print("Ignoring quantile parameter \
                       as ECMWF HRES has no quantile data")
            if ecmwf_hres_param is None:
                print("Please provide a parameter from ECMWF HRES")
                spinner.text = "Input incomplete"
                spinner.fail("💥 ")
                return
            else:
                param = ecmwf_hres_param

        elif model_type == 'ecmwf_ens':
            URL = GET_ENS_ANIMATED_GRAPH_URL
            if quantile is None:
                print("Please select a quantile with parameter from ECMWF ENS")
                spinner.text = "request failed...select a quantile"
                spinner.fail("💥 ")
                return
            else:
                payload['quantile'] = quantile

            if ecmwf_ens_param is None:
                print("Please provide a parameter from ECMWF ENS")
                spinner.text = "request failed"
                spinner.fail("💥 ")
                return
            else:
                param = ecmwf_ens_param

        elif model_type == 'ecmwf_seas':
            URL = GET_SEAS_ANIMATED_GRAPH_URL
            if quantile is None:
                print("Please select a quantile \
                      with parameter from ECMWF SEAS")
                spinner.text = "request failed...select a quantile"
                spinner.fail("💥 ")
                return
            else:
                payload['quantile'] = quantile

            if ecmwf_seas_param is None:
                print("Please provide a parameter from ECMWF SEAS")
                spinner.text = "request failed"
                spinner.fail("💥 ")
                return
            else:
                param = ecmwf_seas_param

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
            URL, stream=True,
            headers=headers, data=json.dumps(payload)
        )
        if response.status_code == 200:
            if is_response_okay:
                export_html_video(response.content, output)
                spinner.text = "Done"
                spinner.ok("✅")
            else:
                spinner.fail("💥 ")

        else:
            print(response.status_code)
            spinner.fail("💥 ")


if __name__ == '__main__':
    main()
