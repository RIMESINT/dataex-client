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

$ get_netcdf_subset_ecmwf_ens.py --params u10 --latbounds 20 40 --lonbounds 80 120 --out filename
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


 


