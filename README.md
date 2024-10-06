## dataex-client API
A client API for using dataex services such as:
- Downloading observation data from dataex.
- Insert observation data into dataex.
- Downloading netcdf subset files of HRES, ENS and IMD WRF forecasts.
- Fetching summary information of observation data.
- Downloading HRES/ENS/IMD WRF forecast analysis region data.

#### Installation

dataex-client can be installed using the following commands
``` bash
$ pip install https://github.com/nzahasan/dataex-client/zipball/master
```
#### Scripts in the package

#### Using dataex_init.py

It can be used to create the `.dataex_auth.json` file which is required for authenticating users. The user is prompted for their dataex username and password.

```
$ dataex_init.py
```

#### Using dataex_netcdf_subset.py

`dataex_netcdf_subset.py` script provides a command line tool for getting a netcdf file subset of ecmwf hres or ens forecasts respectively.

For HRES:
```
$ dataex_netcdf_subset.py --model_type hres --params u10,cp --latbounds 20 40 --lonbounds 80 120 --output filename
```

Options:
```
--model_type: str
              ens, imd_wrf or hres(default) model
            
--params -p : str or list of str (e.g. u10,ssr,cp)
              Single or comma seperated parameter short names 
             
--latbounds -lat : two float values (e.g. 20.2, 60.5)
                   South and North latitude float values space seperated 
             
--lonbounds -lon : two float values (e.g. 100.0, 150.24)
                   West and East latitude float values space seperated 
             
--output : str
           output filename

```

#### List of parameters in ECMWF HRES

The following parameters are available for subsetting in `ECMWF HRES`,

```
    u10, ssr, str, sshf, slhf,
    d2m, v10, t2m, cp, lsp,
    swvl1,swvl2, swvl3, swvl4
```

#### List of parameters in ECMWF ENS

The following parameters are available for subsetting in `ECMWF ENS`,

```
    cp_q5, cp_q25, cp_q50, cp_q75, cp_q95,
    t2m_q5, t2m_q25, t2m_q50, t2m_q75, t2m_q95,
    lsp_q5, lsp_q25, lsp_q50, lsp_q75, lsp_q95
```

#### List of parameters in IMD WRF

The following parameters are available for subsetting in `IMD WRF`,

```
    APCP, T2m, RH2m, U10, V10,
    SWNETB, LWNETB, dbz, cldfra
```

#### Using dataex_insert_obs_data.py 

This script is for inserting observation data into dataex. It takes as input a json file and country id.

```
$ dataex_insert_obs_data.py --country_id 1 --obs_data filename
```
Options:
```
country_id : int
             id number of country
             
obs_data : str
           input csv or excel file
```
#### Format of csv and excel

The column headers in both csv and excel must be `start_time, end_time, value, level_id, parameter_id and station_id`.

```
start_time,end_time,value,level_id,parameter_id,station_id
1995-01-01 00:00,1995-01-02 00:00,30.2,2,3,54
1996-01-01 00:00,1996-01-02 00:00,28.2,2,3,54
```
The time values must be in `YYYY-MM-DD HH:MM` format for both csv and excel files.


#### Using dataex_get_obs_data.py
This script is for getting observation data from dataex. The data can be downloaded in either csv or json format.

```
$ dataex_get_obs_data.py --start_date 1993-01-91 --end_date 1993-02-01 -- station_id 12 --p_id 7 --output_type csv --output filename 
```
Options:
```
start_date : DateTime
             Date in YYYY-MM-DD format
        
end_date : DateTime
           Date in YYYY-MM-DD format
           
station_id : int
             observation station id
            
parameter_id : int 
               parameter id     

output_type : str
              csv, table or json
              
output : str
         output filename

```

#### Using dataex_obs_data_summary.py
This script is for fetching a summary information of the observation data stored in dataex. This data can be downloaded in either json or csv.

```
$ dataex_obs_data_summary.py --output filename --output_type csv
```
Options:
```
output : str
         output file
  
output_type: str
             json or csv    

```
#### Using dataex_region_data_analysis.py 

These scripts allow users to download ecmwf hres and ens forecast analysis region data from dataex. 

```
$ dataex_region_data_analysis.py --model_type <str> --reducer <str> --asset_identifier <str> --unique_field <str> --output_format <str> --output <str>

```

Options:
``` 
    model_type : str
                 ens or hres(default)
                  
    reducer : str
              name of reducer to use

    asset_identifier : str
                       identifier for asset
    
    unique_field : str
                   unique fields in asset

    output_format : str
                    json or xlsx   

    output : str
             output file
```

#### List available reducers

This script allows the user to list the available `reducer` names in forecast analysis.

Usage:

```
$ dataex_list_reducers.py --output_format <str> --output <str>
```
Options:
```

    model_type : str
                 ens, imd_wrf or hres
   
    output_format : str
                    json, table or csv       

    output : str
             output filename
```
             
             

#### List available user assets

This script allows the user to list forecast asset information.


```
$ dataex_list_user_assets.py 
``` 
 


