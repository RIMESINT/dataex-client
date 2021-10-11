## Get Country Info CLI

It can be used to retrieve information such as Id number related to a specific country or all countries available on Dataex. 

###Usage
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
             
The default output format is `table`. Hence, leaving this option out from the command is not a problem.

###Example

```
$ dataex_list_country_info.py --country Bangladesh --output_format  json --output ./country_info.json

```

```
$ dataex_list_country_info.py
```

If country option is not provided then information on all countries in the dataex is returned. 

```
$ dataex_list_country_info.py --country Bangladesh
```
This downloads and displays information on the terminal in table format for Bangladesh. 
