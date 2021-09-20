## dataex-client API
A client API for using dataex.

#### Installation

dataex-client can be installed using the following commands
```
git clone https://github.com/nzahasan/dataex-client.git
cd dataex-client
python3 setup.py install
```

#### Using get_netcdf_subset_ecmwf_hres.py and get_netcdf_subset_ecmwf_ens.py

This package contains `get_netcdf_subset_ecmwf_hres.py` and `get_netcdf_subset_ecmwf_ens.py` scripts. Command line tools for getting a netcdf file subset of ecmwf hres and ens forecasts respectively.

```
$ get_netcdf_subset_ecmwf_hres.py --params u10 --latbounds 20 40 --lonbounds 80 120 --out /path/to/output

$ get_netcdf_subset_ecmwf_ens.py --params u10 --latbounds 20 40 --lonbounds 80 120 --out /path/to/output
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


