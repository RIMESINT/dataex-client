#Check reducers CLI

This script allows the user to list all the available reducer names that can be used in forecast analysis.

Usage:
```
$ dataex_list_reducers.py --model_type <str> --output_format <str> --output <str>
```
Options:
```
    model_type : str
                 ENS/HRES(default) models
    
    output_format : str
                    json, table(default), csv       

    output : str
             output filename

```

## Example

```
$ dataex_check_reducers.py --output_format json --output ./reducers.json
```


