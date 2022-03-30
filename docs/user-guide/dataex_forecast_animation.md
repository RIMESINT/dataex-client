##Forecast Graphics Engine CLI

This script allows to download animated graphs for the following models -

* [X] ECMWF HRES
* [X] ECMWF ENS
* [X] ECMWF SEAS 

###Usage
```
$ dataex_forecast_animation.py --model_type <str> --hres_params <str> --latbounds <float> <float> --lonbounds <float> <float> --output <str>

$ dataex_forecast_animation.py --model_type <str> --ens_params <str> --quantile <str> --latbounds <float> <float> --lonbounds <float> <float> --output <str>

$ dataex_forecast_animation.py --model_type <str> --seas_params <str> --quantile <str> --latbounds <float> <float> --lonbounds <float> <float> --output <str>

```

Unlike single graphs, animation comprises all forecast dates.

!!! Tip
    Option names too long, you can always use their short forms. Check using `--help`

###Options

```

model_type  : str
              model name (ecmwf hres, ens or seas)

ecmwf_hres_params : str
                    name of ecmwf hres parameter
              
ecmwf_ens_params  : str
                    name of ecmwf ens parameter
                    
ecmwf_seas_params : str
                    name of ecmwf seas parameter

quantile    : str
              For ecmwf ens or seas parameters, there are five quantile values to choose,
              'q5', 'q25', 'q50', 'q75', 'q95'
                           
latbounds   : float values
              South and North latitude values space seperated 
                
lonbounds   : float values 
              West and East longitude values space seperated 
           
output      : str
              output filename
```

!!! warning
    - Latitude and longitude values outside the available dataset boundaries will return an error. 
    - Only ecmwf ens or seas parameters can use quantiles option.

The output of this command is a `html` video file which means it can be opened in the web browser. 

!!! info
    The lead days for `ecmwf hres` is 10 days while for `ecmwf ens` is 15 days. And for `ecmwf seas` is 7 months.
    
###Example

For ECMWF HRES,
```
dataex_forecast_animation.py -mt ecmwf_hres -hp total_daily_rainfall -lat 12.55 36.32 -lon 67.68 85.25 -o hres_anime
```
For ECMWF ENS,
```
dataex_forecast_animation.py -mt ecmwf_ens -ep total_daily_rainfall -q q5 -lat 12.55 36.32 -lon 67.68 85.25 -o ens_anime
```
For ECMWF SEAS,
```
dataex_forecast_animation.py -mt ecmwf_seas -sp total_daily_rainfall -q q5 -lat 12.55 36.32 -lon 67.68 85.25 -o seas_anime
```
