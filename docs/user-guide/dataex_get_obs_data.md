## Get Observation Data CLI

This script is for downloading observation data from Dataex server. 
Users can get the desired observation data in the selected format for a specific observation parameter and station.

###Usage
```
$ dataex_get_obs_data.py --start_date <YYYY-MM-DD> --end_date <YYYY-MM-DD> -- station_id <int> --parameter_id <int> --output_type <str> --output <str>
```

###Options
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
                  json, table or csv       

    output : str
             output filename
```

Users can get station and parameter Id numbers using `dataex_obs_station_list.py` and `dataex_obs_parameter_list.py` respectively.
Leaving the option `output_type` will default to `table`. 



### Example

```
$ get_obs_data.py --start_date 1994-11-01 --end_date 1994-12-10 -- stn_id 11 --p_id 4 --output_type csv --output ./obs_data.csv
```

It goes without saying that the `start_date` must be a date that is earlier than the `end_date`. The time period should be within 180 days. In case the time period is beyond 180 days, the server just returns a truncated observation dataset of 180 days instead.

```
$ get_obs_data.py --start_date 1994-11-01 --end_date 1994-12-10 -- stn_id 11 --p_id 4
```
Observation data are displayed in tabular form in the terminal.
