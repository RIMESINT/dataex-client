##Get region data analysis CLI

This script allows the user to download region data analysis of `HRES, ENS or SEAS` models.

To find the available reducer names for a particular model, you can use `dataex_list_reducers.py`.

###Usage
```
$ dataex_region_data_analysis.py --model_type <str> --reducer <str> --asset_identifier <str> --unique_field <str> --output_format <str> --output <str>
```

###Options

    model_type : str
                 ENS, HRES(default) or SEAS
   
    reducer : str
              name of reducer to use

    asset_identifier : str
                       identifier for asset
    
    unique_field : str
                   unique fields in asset

    output_format : str
                    json or xlsx       

    output : str
             output filename
             
###Example

```
$ dataex_get_ecmwf_hres_region_data.py --reducer rainfall_daily_weighted_average -ai e02d7063-7b91-4bfd-958f-00cb099860a0 -uf ADM2_EN -of xlsx -o ./hres_region_data.xlsx
```

Here, the short option names are utilized. Since, model type is not explicitly specified, it defaults to `HRES`. The output is an excel file which will contain province wise data in different sheets. 
