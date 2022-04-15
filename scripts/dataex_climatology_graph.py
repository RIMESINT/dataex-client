#!/usr/bin/env python3

import json
import click
import requests 

from yaspin import yaspin

from dataexclient import auth_helper
from dataexclient.config import GET_STATION_CLIMATOLOGY_URL
from dataexclient.utils import export_graph, is_response_okay


@click.command()
@click.option('--station_id', '-sid',
               required=True,  
               help='Id of the station'
)
@click.option('--output', '-o',
               required=True,  
               help='Name for file'
)

def main(station_id, output):
    payload = dict()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token(),
    }
    payload['station_id'] = station_id
    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(GET_STATION_CLIMATOLOGY_URL, stream=True, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            if is_response_okay(response):
                export_graph(response.content, output)
                spinner.text = "Done"    
                spinner.ok("✅")
            else:
                spinner.fail("💥 ")   

        else:
            print(response.status_code)
            spinner.fail("💥 ")
    
    
    
    
if __name__=='__main__':
    main()
