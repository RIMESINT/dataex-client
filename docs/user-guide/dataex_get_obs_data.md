# Get Observation Data CLI

This script allows the user to get observation data from Dataex server. 
This tool downloads the desired observation data in the selected format.

Usage:
```
$ dataex_get_obs_data.py --start_date <YYYY-MM-DD> --end_date <YYYY-MM-DD> -- station_id <int> --parameter_id <int> --output_type <str> --output <str>
```

Options:
```
    start_date : DateTime
                 Date in YYYY-MM-DD format
        
    end_date : DateTime
               Date in YYYY-MM-DD format
               
    station_id : int
                 station id
            
    parameter_id : int 
                   parameter id     

    output_type : str
                  json or csv       

    output : str
             output filename
```

## Example

```
$ get_obs_data.py --start_date 1994-11-01 --end_date 1994-12-10 -- stn_id 11 --p_id 4 --output_type csv --output ./obs_data.csv
```
