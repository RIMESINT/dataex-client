## dataex-client API
A client API for using dataex services such as:
- Getting observation data from dataex.
- Insert observation data into dataex.
- Getting netcdf subset files of HRES and ENS forecasts.
- Getting summary information of observation data.

#### Installation

dataex-client can be installed using the following commands
```
$ git clone https://github.com/nzahasan/dataex-client.git
$ cd dataex-client
$ python3 setup.py install
```

#### Using get_netcdf_subset_ecmwf_hres.py and get_netcdf_subset_ecmwf_ens.py

This package contains `get_netcdf_subset_ecmwf_hres.py` and `get_netcdf_subset_ecmwf_ens.py` scripts. Command line tools for getting a netcdf file subset of ecmwf hres and ens forecasts respectively.

```
$ get_netcdf_subset_ecmwf_hres.py --params u10 --latbounds 20 40 --lonbounds 80 120 --out filename

$ get_netcdf_subset_ecmwf_ens.py --params t2m_q50 --latbounds 20 40 --lonbounds 80 120 --out filename
```

Options:
```
--params : str or list of str
           Single or comma seperated parameter short names 
             
--latbounds : first float is for south and second float is for north
              South and North latitude values space seperated 
             
--lonbounds : first float is for south and second float is for north 
              West and East latitude values space seperated 
             
--out : str
        output filename

```

### List of parameters in ECMWF HRES

The following parameters are available for subsetting in `ECMWF HRES`,

```
    u10, ssr, str, sshf, slhf
    d2m, v10, t2m, cp, lsp
    swvl1,swvl2, swvl3, swvl4
```

### List of parameters in ECMWF ENS

The following parameters are available for subsetting in `ECMWF ENS`,

```
    cp_q5, cp_q25, cp_q50, cp_q75, cp_q95,
    t2m_q5, t2m_q25, t2m_q50, t2m_q75, t2m_q95,
    lsp_q5, lsp_q25, lsp_q50, lsp_q75, lsp_q95
```

### Using insert_obs_data.py 

This script is for inserting observation data into dataex. It takes as input a json file and country id.

```
$ get_obs_data.py --country_id 1 --obs_data filename
```
Options:
```
country_id : int
             id number of country
             
obs_data : str
           file either csv or excel  
```
Format of csv and excel

The column headers in both csv and excel must be `start_time, end_time, value, level_id, parameter_id and station_id`.

```
start_time,end_time,value,level_id,parameter_id,station_id
1995-01-01 00:00,1995-01-02 00:00,30.2,2,3,54
1996-01-01 00:00,1996-01-02 00:00,28.2,2,3,54
```
The time values must be in `YYYY-MM-DD HH:MM` format for both csv and excel files.


### Using get_obs_data.py
This script is for getting observation data from dataex. The data can be downloaded in either csv or json format.

```
$ get_obs_data.py --start_date 1993-01-91 --end_date 1993-02-01 -- stn_id 12 --p_id 7 --output_type csv --out filename 
```
Options:
```
start_date : DateTime
             Date in YYYY-MM-DD format
        
end_date : DateTime
           Date in YYYY-MM-DD format
           
stn_id : int
         station id
            
p_id : int 
       parameter id     

output_type : str
              csv or json
              
out : str
      output filename

```

### Using fetch_obs_summary.py
This script is for fetching a summary information of the observation data stored in dataex. This data can be downloaded in either json or csv.

```
$ fetch_obs_summary.py --out filename --output_type csv
```
Options:
```
out : str
      name of output file 
      
output_type: str
             json or csv    

```


 


