## Insert observation data CLI

This script allows the user to upload station specific observation data into Dataex server. 
It takes as input either a csv or excel file containing the observations along with the country id number as the command arguments.

!!! info
    To get the country id numbers, you can use `dataex_list_country_info.py` command.

###Usage
```
$ dataex_insert_obs_data.py --country_id <int> --obs_data <str> 
```

!!! Tip
    Option names too long, you can always use their short forms. Check using `--help`
    

###Options

```
country_id : int
             id number of country
                 
obs_data   : str
             input file is either csv or excel
```          
###Example

```
dataex_insert_obs_data.py --country_id 5 --obs_data ./input.csv
```
Here, the input observation data is provided in csv format using `--obs_data` option.

###Input file details

The column headers in both csv and excels must be:

`start_time, end_time, value, level_id, parameter_id and station_id`


- Start and end time denote the time of recorded observation.
- The start and time values must be in `YYYY-MM-DD HH:MM` format for both csv and excel files.
- Accumulated parameters such as rainfall have different start and end times while instant parameters have the same start and end times.
- Every parameter has a distinct id. Find the details using `dataex_obs_parameter_list.py` command.
- The level id is used for identifying observation measurement levels such as surface level, 2m or 10 m.
- Every station has a unique id assigned to it. Use the `dataex_obs_station_list.py` command to retrieve it.


###level_id
This is related to the level of measurement regarding an observation. The table below shows the id numbers of levels in Dataex:

|name|full_name|id|
|----|---------|--|
|sfc|Surface|1
|2m|2 Meter|2
|3m|3 Meter|3

###start_time and end_time

Determing these two times depends on the observation itself. If the observation is 24 hourly then these times should account for that period.
For example, if the start_time is 1995-01-01 00:00, then end_time is 1995-01-02 00:00, when the observation time period is 24 hours. 
In case there is only 15 minute difference then it would be 1995-01-01 00:15. Further, when it is an instant parameter type then both times are same.


!!! warning
    
    Please adhere strictly to the format below used in the examples for successful execution of the command.

###CSV file format

```
start_time,end_time,value,level_id,parameter_id,station_id
1995-01-01 00:00,1995-01-02 00:00,30.2,2,3,54
1996-01-01 00:00,1996-01-02 00:00,28.2,2,3,54
```


###Excel file format

|start_time| end_time | value | level_id | parameter_id | station_id |
|----------|----------|-------|----------|--------------|------------|
|1995-01-01 00:00 | 1995-01-02 00:00 | 30.2 | 2 | 3 | 54
|1996-01-01 00:00| 1996-01-02 00:00| 28.2 | 2 | 3 | 54


This file format ensures a standard input format for all observations. Raw observations can be formatted to follow this standard for easy upload and usage in dataex.



