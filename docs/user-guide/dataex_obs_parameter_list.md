# Get Parameter Info CLI

This script allows the user to get station's parameter information such as ID number and name from Dataex server. 
This tool can download in either csv or json file.

Usage:
```
$ dataex_obs_parameter_list.py --station_id <int> --output_type <str> --output <str>
```
Options:
```
    station_id : int
                 station id     

    output_type : str
                  json, table(default), csv       

    output : str
             output filename

```
## Example

```
$ dataex_obs_parameter_list.py --station_id 53 --output_type csv --output ./param_info.csv
```

