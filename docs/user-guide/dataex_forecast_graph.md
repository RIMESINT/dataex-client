##Forecast Graphics Engine CLI

This script allows to download single day forecast graphs for the following models -

* [X] ECMWF HRES
* [X] ECMWF ENS
* [X] ECMWF SEAS 

###Usage
```
$ dataex_forecast_graph.py --model_type <str> --ecmwf_hres_params <str> --day <str> --latbounds <float> <float> --lonbounds <float> <float> --output <str>

$ dataex_forecast_graph.py --model_type <str> --ecmwf_ens_params <str> --quantile <str> --day <str> --latbounds <float> <float> --lonbounds <float> <float> --output <str>

$ dataex_forecast_graph.py --model_type <str> --ecmwf_seas_params <str> --quantile <str> --month <str> --latbounds <float> <float> --lonbounds <float> <float> --output <str>

```

Get the names of available parameters using `dataex_forecast_graph_params.py`. Check the documentation on [dataex_forecast_graph_params](dataex_forecast_graph_params.md) for further details. 

!!! Tip
    Option names too long, you can always use their short forms. Check using `--help`

###Options

```

model_type  : str
              model name (ecmwf_hres, ecmwf_ens or ecmwf_seas)

ecmwf_hres_params : str
                    name of ecmwf hres parameter
              
ecmwf_ens_params  : str
                    name of ecwmf ens parameter
                    
ecmwf_seas_params : str
                    name of ecmwf seas parameter

quantile    : str
              For both ecmwf ens and seas parameters, there are five quantile values to choose,
              'q5', 'q25', 'q50', 'q75', 'q95'

day         : str
              This represents the day of forecast with '1' being for first day and so on. 
              
month       : str
              This represents the month of forecast with '1' being for first month and so on. Only applies to ECMWF SEAS
                           
latbounds   : float values
              South and North latitude values space seperated 
                
lonbounds   : float values 
              West and East longitude values space seperated 
           
output      : str
              output filename
```

!!! warning
    - Latitude and longitude values outside the available dataset boundaries will return an error. 
    - Only `ecmwf_ens` and `ecmwf_seas` parameters can use quantiles option.

The output is a `png` image file. Choosing the day of the forecast gives you the graph for the desired parameter of that day.

!!! info
    The lead days for `ecmwf hres` is 10 days while for `ecmwf ens` is 15 days and `ecmwf_seas` is 7 months.
    
###Example:
For ECMWF ENS,
```
dataex_forecast_graph.py -mt ecmwf_ens -ep temperature_max -q q25 -d 1 -lat 12.55 36.32 -lon 67.68 85.25 -o graph_ens
```
For ECMWF HRES,
```
dataex_forecast_graph.py -mt ecmwf_hres -hp temperature_max -d 1 -lat 12.55 36.32 -lon 67.68 85.25 -o graph_hres
```
For ECMWF SEAS,
```
dataex_forecast_graph.py -mt ecmwf_seas -sp total_daily_rainfall -m 1 -q q5 -lat 12.55 36.32 -lon 67.68 85.25 -o graph_seas
```



