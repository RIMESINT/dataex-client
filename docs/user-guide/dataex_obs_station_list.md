## Get Station List CLI

This script allows the user to get country's station information such as ID number and name from Dataex server. This tool can download output in either csv or json file.

Usage:
```
$ dataex_obs_station_list.py --country_id <int> --not_empty --output_type <str> --output <str>
```

Options:
```
    country_id : int
                 country id     

    output_type : str
                  json, table(default), csv    
                  
    not_empty : set to only get only those stations with data
    
    empty : set to get any station even if they are empty      

    output : str
             output filename

```

Each country has a number of stations with their own distinct id numbers. Using the empty/not_empty option, one can choose if they want to download information of stations having related observations or not. 


## Example
```
$ dataex_obs_station_list.py --country_id 3 --empty --output_type csv --output ./station_info.csv
```

