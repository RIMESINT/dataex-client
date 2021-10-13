##Get region data analysis CLI

This script allows the user to download region data analysis of following models.

* [X] HRES
* [X] ENS
* [ ] SEAS

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
          
The model type input is case-insensitive. Hence, ENS or ens are both valid.
          
!!! Info 
    User asset information such as asset identifier and unique field can obtained from `dataex_list_user_assets.py`. 
         
###Example

```
$ dataex_get_ecmwf_hres_region_data.py -r rainfall_daily_weighted_average -ai e02d7063-7b91-4bfd-00cb099860a0 -uf ADM2_EN -of xlsx -o ./hres_region_data.xlsx
```

Here, the short option names are utilized. Since, model type is not explicitly specified, it defaults to `HRES`. The output is an excel file which will contain province wise data in different sheets. 
