## Get Station List CLI

This script allows the user to get country's station information such as ID number and name from Dataex server. This tool can download output in either csv or json file or show it in tabular form.

###Usage
```
$ dataex_obs_station_list.py --country_id <int> --not_empty --output_type <str> --output <str>
```

###Options
```
    country_id : int
                 country id     

    output_type : str
                  json, table(default), csv    
                  
    not_empty : use to only get only those stations with data
    
    empty : use to get any station even if they are empty      

    output : str
             output filename

```

Each country has a number of stations with their own distinct id numbers. Using the empty/not_empty option, one can choose if they want to download information of stations having related observations or not. The `empty` and `non-empty` options are boolean flags which can be enabled or disabled. `empty` is the default state. 
`table` output is the default in case no other value is entered.


### Example
```
$ dataex_obs_station_list.py --country_id 3 --non_empty --output_type csv --output ./station_info.csv
```
This will download a list of observation stations and their related information for country with `id` number 3 and since output type is `csv`, the data will be stored in a csv file with name `station_info.csv` in the current directory. Since, `non_empty` flag is set, only those stations with observations are retrieved. 


To get a list of country Id numbers, you can use `dataex_list_country_info.py`. This will help you know about the countries available in dataex. 
