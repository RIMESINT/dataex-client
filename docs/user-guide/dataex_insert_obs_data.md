## Insert observation data CLI

This script allows the user to upload observation data into Dataex server. 
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
             input file either csv or excel   
```          
###Example

```
$ dataex_insert_obs_data.py --country_id 5 --obs_data ./input.csv
```
Here, the input observation data is provided in csv format using `--obs_data` option.

###Input file details

The column headers in both csv and excels must be:

`start_time, end_time, value, level_id, parameter_id and station_id`


- Start and end time denote the date of recorded observation. 
- Accumulated parameters have different start and end times while instant parameters have the same start and end times.
- Every parameter has a distinct id.
- The level id is used for identifying observation levels such as surface level, 2m or 10 m.
- Every station has a unique id assigned to it.  

The time values must be in `YYYY-MM-DD HH:MM` format for both csv and excel files.

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




