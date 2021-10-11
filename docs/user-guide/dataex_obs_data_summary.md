## Fetch observation data summary CLI

This script allows the user to fetch summary of observation data statistics from Dataex server.
A sample of the information that is retrieved from the dataex server can be seen in the table below:

|country| No. of Stations Sharing Data | Data Available Period | Total Records (Daily) | % Missing Data
|----------|----------|-------|----------|--------------|
|Bangladesh | 47 | 1981-01-01 to 2020-01-01 | 2830011 | 0.6%
|Nepal| 16 | 1981-01-01 to 2021-01-01 | 1122690 | 12.1%



###Usage
```
$ dataex_obs_data_summary.py --output <str> --output_type <str>
```
###Options
```
    output : str
             name of output file  
              
    output_type: str 
                 json, table(default), csv   
```

The default output type is `table` format. The two options are not required and can be ignored unless the user prefers csv or json.

### Example
```
$ dataex_obs_data_summary.py --output ./summary.csv --output_type csv

```
Here, the observation summary data is downloaded in `csv` format. The file is saved as `summary.csv` in the current directory. If no .csv extension is provided, it is appended by the program.  

```
$ dataex_obs_data_summary.py
```

This would download the data in `table` format and display in that form on the terminal itself.
