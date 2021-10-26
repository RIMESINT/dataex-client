
<img alt="Dataex" src="img/dataex_logo.svg" width="800px" style="display: block; margin: 0 auto 0 auto">

# Welcome to Dataex Client API 

A client API for using dataex services such as:

- Download observation data from dataex.
- Insert observation data into dataex.
- Download netcdf subset files of HRES/ENS/SEAS forecasts.
- Download summary information of observation data.
- List reducer names and user asset information in forecast analysis.
- Download forecast region analysis data of ECMWF ENS/HRES/SEAS region data.

### Installation

Dataex-client API can be installed using the following command,
```
pip install https://github.com/nzahasan/dataex-client/zipball/master
```

### Commands

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

### Example

Let's take a look at a quick example of one of the above commands. It's as easy as typing the command into your favourite terminal. Suppose we want to download a netCDF subset file from model `hres` for parameters `u10, swvl1, t2m`. We can use the following command, 

```
$ dataex_netcdf_subset.py --model_type hres --params u10,swvl1,t2m --latbounds 40.3 60.0 --lonbounds 90.0 120.0 --output /home/user/hres_subset.nc

``` 
Alternatively, you can use short forms of the option names used in the above command. 

### Support

For support please email us at support@rimes.int. Make sure to include the specific problem in the subject of the mail.

### Security

If you believe you've found something in the dataex client API which has security implications, pleas send a description of the issue via email to support@rimes.int.


### License

MIT License

Copyright © 2021 RIMES

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

