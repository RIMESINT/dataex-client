"""Helper functions used throughout Dataex API"""
import json

import pandas as pd

from tabulate import tabulate

def export_json(data, output=None):
    """Creates a json file as output"""
    if output is not None:
        if not output.endswith('.json'):
            output += '.json'
            with open(f'{output}', 'w') as f:
                json.dump(data, f)
    else:
        print(data)
    

def export_csv(data, output=None):
    """Creates a csv file as output"""
    df = pd.DataFrame(data)
    if output is not None:
        if not output.endswith('.csv'):
            output += '.csv'
            df.to_csv(output, index=False)
    else:
        print(data)


def export_table(data, output=None, tablefmt='psql'):
    """Creates a table as output"""
    df = pd.DataFrame(data)
    table = tabulate(df, headers='keys', showindex=False, tablefmt=tablefmt)
    if output is not None:
        with open(output, 'w') as outfile:
            outfile.write(table)
    else:
        print(table)


def export_nc(data, output):
    if not output.endswith('.nc'):
        output += '.nc'

    with open(f'{output}', 'wb') as f:
        f.write(data)


def export_graph(data, output): # data is the content of response from server
    if not output.endswith('.png'):
        output += '.png'

    with open(f'{output}', 'wb') as f:
        f.write(data)


def export_html_video(data, output): # data is the content of response from server
    if not output.endswith('.html'):
        output += '.html'
              
    with open(f'{output}', 'wb') as f:
        f.write(data)


def is_response_okay(response):
    """check if repsonse has error"""
    if response.headers['content-type'] == "application/json":
        data = response.json()
        print(data['error'], data['message'])
        return False
    return True


def check_error(data):
    """Check if there is error in response"""
    if 'error' in data:
        if data['error'] is None:
            print(data['message']) 
            return False
        else:
            print(data['error'],'-> ',data['message'])
            return True
    return False


def check_output_format(data, output=None, output_format='json'):
    """Check output format and call the right export func"""
    if output_format == 'json':
        export_json(data, output)
    elif output_format == 'csv':
        export_csv(data, output)
    elif output_format == 'table':
        export_table(data, output)
    elif output_format == 'xlsx':
        json_to_excel(data, output)


def create_json(file, country_id):
    """
    Creates a json file for inserting
    observation data to Dataex
    
    Parameters
    ----------
    file : object
           dataframe
    country_id: str
                Id of country entered by the user
   
    Returns
    --------
    json 
          a json file containing rows of observation data
    """ 
    
    obs_data_json = {}
    data = []
    row = {}
    for i in range(len(file)):
        row['station_id'] = int(file.iloc[i]['station_id'])
        row['parameter_id'] = int(file.iloc[i]['parameter_id'])
        row['level_id'] = int(file.iloc[i]['level_id'])
        row['start_time'] = file.iloc[i]['start_time'] + 'Z'
        row['end_time'] = file.iloc[i]['end_time'] + 'Z'
        row['value'] = int(file.iloc[i]['value'])
        data.append(row)
        row = {}

    obs_data_json['country_id'] = country_id

    obs_data_json['data'] = data
    return obs_data_json


def json_to_excel(data, name):
    """
    Converts json file containing 
    analyzed reduced forecast data from 
    Dataex to excel format

    Parameters
    ----------
    file : object
           dataframe

    name: reducer name

    Returns
    --------
    xlsx 
          an excel file containing analyzed reduced forecast data
    """
    print('converting json to excel...')
    if not name.endswith('.xlsx'):
        name += '.xlsx'

    writer = pd.ExcelWriter(name)
    start_dates = []
    end_dates = []
    _values= []

    for key, val in data['r_data'].items(): # r_data is the key to access data to iterate over 
        for inner_key, inner_val in val.items():
            
            if inner_key=='time':
                for dates in inner_val:
                    start_dates.append(dates[0])
                    end_dates.append(dates[1])
                    
            
            if inner_key=='value':
                for value in inner_val:
                    _values.append(value)
        
            
        df_start_dates = pd.DataFrame(start_dates, columns=['start_date'])
        df_end_dates = pd.DataFrame(end_dates, columns=['end_date'])
        df_values = pd.DataFrame(_values, columns=['values'])
        df = pd.concat([df_start_dates, df_end_dates, df_values],axis=1)
        df.to_excel(writer, sheet_name=key, index=False)
        _values = []
        start_dates = []
        end_dates = []
    
    writer.close()