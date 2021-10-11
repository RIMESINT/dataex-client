## Get Parameter Info CLI

This script allows the user to get station's parameter information such as ID number and name from Dataex server. 
This tool can download in either csv or json file.

Observation station Id numbers can be obtained by executing `dataex_obs_station_list.py`.

###Usage
```
$ dataex_obs_parameter_list.py --station_id <int> --output_type <str> --output <str>
```
###Options
```
    station_id : int
                 station id     

    output_type : str
                  json, table(default), csv       

    output : str
             output filename

```
If `output_type` is not specified then it defaults to `table`. Further, in this case, if output is also not specified, the data is displayed in tabular form in the terminal.

### Example

```
$ dataex_obs_parameter_list.py --station_id 53 --output_type csv --output ./param_info.csv
```
Here, data is downloaded in a `csv` file named as `param_info.csv` in the current directory.


```
$ dataex_obs_parameter_list.py --station_id 53
```
Here, `table` is default and tabular data is displayed in the terminal. 
