## Get Station List CLI

This script allows the user to get country's station information such as ID number and name from Dataex server. This tool can download output in either csv or json file or show it in tabular form.

!!! Info 
    To get a list of country Id numbers, you can use `dataex_list_country_info.py`. This will help you know about the countries available in dataex. 

###Usage
```
$ dataex_obs_station_list.py --country_id <int> --not_empty --output_format <str> --output <str>
```

!!! Tip
    Option names too long, you can always use their short forms. Check using `--help`
    
###Options
```
not_empty/empty   : flag to get only those stations with data or all 

output_format     : str
                    json, table or csv  
              
country_id        : int
                    country id     

output            : str
                    output filename

```

Each country has a number of stations with their own distinct id numbers. Using the empty/not_empty option, one can choose if they want to download information of only those stations with observations or all.

!!! info
    The `empty` and `non-empty` options are boolean flags which can be enabled or disabled. `empty` is the default state. 



### Example
```
$ dataex_obs_station_list.py --country_id 3 --non_empty --output_format csv --output ./station_info.csv
```
This will download a list of observation stations and their related information for country with `id` number 3 and since output type is `csv`, the data will be stored in a csv file with name `station_info.csv` in the current directory. Since, `non_empty` flag is set, only those stations with observations are retrieved.