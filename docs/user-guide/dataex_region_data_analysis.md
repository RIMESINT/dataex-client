##Get region data analysis CLI

This script allows the user to download region data analysis of following models.

* [X] ECMWF HRES
* [X] ECMWF ENS
* [ ] ECMWF SEAS

!!! info
    To find the available reducer names for a particular model, you can use `dataex_list_reducers.py`.

###Usage
```
$ dataex_region_data_analysis.py --model_type <str> --reducer <str> --asset_identifier <str> --unique_field <str> --output_format <str> --output <str>
```

!!! Tip
    Option names too long, you can always use their short forms. Check using `--help`
    

###Options
```

asset_identifier : str
                   identifier for asset
                   
unique_field     : str
                   unique fields in asset

output_format    : str
                   json or xlsx      
                   
model_type       : str
                   Model names

reducer          : str
                   name of reducer to use
                   
output           : str
                   output filename
                   
```
          
The model type input is case-insensitive. Hence, ECMWF_ENS or ecmwf_ens are both valid.
          
!!! Info 
    User asset information such as asset identifier and unique field can obtained from `dataex_list_user_assets.py`. 
         
###Example

```
python dataex_region_data_analysis.py -mt ecmwf_hres -r rainfall_daily_weighted_average -ai e02d7063-7b91-4bfd-958f-00cb099860a0 -uf ADM2_EN -of xlsx -o ./hres_region_data.xlsx
```

Here, the short option names are utilized. The output is an excel file.
