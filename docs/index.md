
<img alt="Dataex" src="img/dataex_logo.svg" width="800px" style="display: block; margin: 0 auto 0 auto">

# Welcome to Dataex Client API 

A client API for using dataex services such as:

- Download observation data from dataex.
- Insert observation data into dataex.
- Download netcdf subset files of HRES/ENS/SEAS forecasts.
- Download summary information of observation data.
- List reducer names and user asset information in forecast analysis.
- Download forecast region analysis data of ECMWF ENS/HRES/SEAS region data.

## Installation

Dataex-client API can be installed using the following command,
```
pip install https://github.com/nzahasan/dataex-client/zipball/master
```

## Commands

* [x] `dataex_init.py` - Create `.dataex_auth.json` file for dataex user authentication
* [x] `dataex_netcdf_subset.py` - Download ECMWF HRES/ENS/SEAS model forecasts.
* [x] `dataex_get_obs_data.py` - Download observation data.
* [x] `dataex_obs_data_summary.py` - Download summary information of observation data.
* [x] `dataex_insert_obs_data.py` - Upload observation data.
* [x] `dataex_list_country_info.py` - Retrieve country Id, name information
* [x] `dataex_obs_station_list.py` - Retrieve station information of a specific country
* [x] `dataex_obs_parameter_list.py` - Retrieve a list of parameter information of a specific station
* [x] `dataex_list_user_assets.py` - Retrieve user assets available for use in forecast analysis
* [x] `dataex_list_reducers.py` - Retrieve reducer names available for use in forecast analysis
* [x] `dataex_region_data_analysis.py` - Download ECMWF HRES/ENS/SEAS model forecast region data analysis 
