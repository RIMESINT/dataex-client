##Get Station Climatology CLI

Use to download the climatology graph of a station present in DataEx for the duration of observations available. 

###Usage
```
$ python dataex_climatology_graph.py --station_id <str> --output <str>

```


!!! Tip
    Option names too long, you can always use their short forms. Check using `--help`

###Options

```

station_id  : str
              Id of desired station

output      : str
              output filename
```

    
###Example:
```
python dataex_climatology_graph.py -sid 30 -o clim
```
Downloads climatology graph of station with id number 30. 

