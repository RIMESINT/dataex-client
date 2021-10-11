# Get NetCDF Subset CLI

This script allows the user to get a subset of ECMWF HRES/ENS/SEAS data. 
This tool downloads the data in netCDF file.

Usage:
```
$ dataex_netcdf_subset.py --model_type <str> --params <str>,<str> --latbounds <float> <float> --lonbounds <float> <float> --output <str>

```

Options:
```

    model_type, mt : str
                 ENS/HRES(default)/SEAS model
                 
    params, p : str or list of str
                Single or comma seperated parameter short names 
             
    latbounds, lat : float values
                     South and North latitutde values space seperated 
                
    lonbounds, lon : float values 
                     West and East longitude values space seperated 
                
    output, o : str
                output filename
 
```

## Example
```
$ dataex_netcdf_subset.py --model_type ens  --params u10,swvl1,t2m --latbounds 40.3 60.0 --lonbounds 90.0 120.0 --output /home/user/hres_subset.nc
```

## List of parameters in ECMWF HRES

The following parameters are available for subsetting in `ECMWF HRES`,

```
    u10, ssr, str, sshf, slhf,
    d2m, v10, t2m, cp, lsp,
    swvl1,swvl2, swvl3, swvl4
```

## List of parameters in ECMWF ENS

The following parameters are available for subsetting in `ECMWF ENS`,

```
    cp_q5, cp_q25, cp_q50, cp_q75, cp_q95,
    t2m_q5, t2m_q25, t2m_q50, t2m_q75, t2m_q95,
    lsp_q5, lsp_q25, lsp_q50, lsp_q75, lsp_q95
```
