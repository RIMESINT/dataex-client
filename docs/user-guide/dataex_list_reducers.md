##Check reducers CLI

This script allows the user to list all the available reducer names that can be used in forecast analysis depending on the model type:

- HRES
- ENS
- SEAS


###Usage
```
$ dataex_list_reducers.py --model_type <str> --output_format <str> --output <str>
```
###Options
```
    model_type : str
                 ENS/HRES(default)/SEAS models
    
    output_format : str
                    json, table(default), csv       

    output : str
             output filename

```

For model types, `HRES` is the default. `--output_format` option if not used, defaults to `table` and then the downloaded data is just displayed on terminal in case `output` option is also left out. 

### Example

```
$ dataex_check_reducers.py --output_format json --output ./reducers.json
```
Here, a json file stores the downloaded data. The model type is `HRES` since it is the default.  

```
$ dataex_check_reducers.py --model_type ENS 
```
Model type is specified as `ENS`. The output format is `table` as it is the default. 
