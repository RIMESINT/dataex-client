# Get Country Info CLI

It can be used to retrieve information such as Id number related to a specific country or all countries available on Dataex. 

Usage:
```
$ dataex_list_country_info.py --country <str> --output_format <str> --output <str>
```

Options:

    country : str
              name of country      

    output_format : str
                    json, table(default),csv       

    output : str
             output filename

## Example

```
$ dataex_list_country_info.py --country Bangladesh --output_format  json --output ./country_info.json

```
If country option is not provided then every information on all countries in the dataex is returned. 
