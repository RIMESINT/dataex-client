#!/usr/bin/env python3


import json
import pandas as pd
from dataexclient import auth_helper
from dataexclient.config import LIST_SYSTEM_STATES_URL
import requests
from tabulate import tabulate
import click
from yaspin import yaspin


def main():
    payload = dict()

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth_helper.get_token()
    }

    with yaspin(text="Downloading...", color="yellow") as spinner:
        response = requests.post(LIST_SYSTEM_STATES_URL, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            data = response.json()

            if 'error' in data:
                if data['error'] is None:
                    print(data['message'])    
                    spinner.text = "Done"
                    spinner.ok("✅")
                else:
                    print(data['error'],'-> ',data['message'])
                    spinner.fail("💥 ")


            df = pd.DataFrame(data['system_states'])
            table = tabulate(df, headers='keys', showindex=False, tablefmt='pretty')
            print(table)
 
        else:
            print(response.status_code)
            spinner.fail("💥 ")


if __name__=='__main__':
    main()


