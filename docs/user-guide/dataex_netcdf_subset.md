## Get NetCDF Subset CLI

This script allows the user to get a netCDF subset of model type:

* [X] HRES
* [X] ENS
* [ ] SEAS 


###Usage
```
$ dataex_netcdf_subset.py --model_type <str> --params <str>,<str> --latbounds <float> <float> --lonbounds <float> <float> --output <str>

```
!!! Tip
    Option names too long, you can always use their short forms. Check using `--help`
    
    
###Options

```
model_type : str
             model name
                 
params : str or list of str
         Single or comma seperated parameter short names 
             
latbounds : float values
            South and North latitutde values space seperated 
                
lonbounds : float values 
            West and East longitude values space seperated 
                
output : str
         output filename
```

 

!!! warning
    Latitude and longitude values outside the available dataset boundaries will return an error. 

### List of parameters in ECMWF HRES

The following parameters are available for subsetting in `ECMWF HRES`,

```
    u10, ssr, str, sshf, slhf,
    d2m, v10, t2m, cp, lsp,
    swvl1,swvl2, swvl3, swvl4
```

### List of parameters in ECMWF ENS

The following parameters are available for subsetting in `ECMWF ENS`,

```
    cp_q5, cp_q25, cp_q50, cp_q75, cp_q95,
    t2m_q5, t2m_q25, t2m_q50, t2m_q75, t2m_q95,
    lsp_q5, lsp_q25, lsp_q50, lsp_q75, lsp_q95
```
There are five quantiles available for each parameter in `ECMWF ENS`. 


### Example
```
$ dataex_netcdf_subset.py --model_type hres --params u10,swvl1,t2m --latbounds 40.3 60.0 --lonbounds 90.0 120.0 --output /home/user/hres_subset.nc
```
The model type input is case-insensitive. Here, only three parameters are provided. If model_type was not provided then it defaults to `HRES` model. So, it is important to provide the correct parameter list or name to avoid failure. 

```
$ dataex_netcdf_subset.py --model_type ens --params cp_q25 --latbounds 40.3 60.0 --lonbounds 90.0 120.0 --output /home/user/hres_subset.nc
```
Just one parameter related data is requested above.

