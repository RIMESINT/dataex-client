##List reducers CLI

This script allows the user to list all the available reducer names that can be used in forecast analysis depending on the model type:

- [X] ECMWF HRES
- [X] ECMWF ENS
- [ ] ECMWF SEAS


###Usage
```
$ dataex_list_reducers.py --model_type <str> --output_format <str> --output <str>
```

!!! Tip
    Option names too long, you can always use their short forms. Check using `--help`
    
###Options
```

output_format : str
                json, table, csv 
                
model_type    : str
                model name  

output        : str
                output filename

```

For model types, the name is case insensitive but you must stick to the provided choices which are `ecmwf_ens`, `ecmwf_hres` and `ecmwf_seas`.

 `--output_format` option if not used, defaults to `table` and then the downloaded data is displayed in the terminal when case `output` option is also left out. 

!!! Info
    The model type names are case-insensitive. For instance, ecmwf_hres or ECMWF_HRES are both valid. 


### Example

```
$ dataex_list_reducers.py --model_type ecmwf_hres --output_format json --output ./reducers.json
```
Here, a json file is used to store the downloaded data. The model type is `ecmwf_hres`.

```
$ dataex_list_reducers.py --model_type ECMWF_ENS 
```

Model type is specified as `ECMWF ENS`. The output format is `table` which is the default. 
