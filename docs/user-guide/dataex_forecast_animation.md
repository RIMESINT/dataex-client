##Forecast Graphics Engine CLI

This script allows to download animated graphs for the following models -

* [X] HRES
* [X] ENS
* [ ] SEAS 

###Usage
```
$ dataex_forecast_animation.py --model_type <str> --hres_params <str> --latbounds <float> <float> --lonbounds <float> <float> --output <str>

$ dataex_forecast_animation.py --model_type <str> --ens_params <str> --quantile <str> --latbounds <float> <float> --lonbounds <float> <float> --output <str>

```

Unlike single graphs, animation comprises all forecast dates.

!!! Tip
    Option names too long, you can always use their short forms. Check using `--help`

###Options

```

model_type  : str
              model name (hres, ens or seas)

hres_params : str
              name of hres parameter
              
ens_params  : str
              name of ens parameter

quantile    : str
              For ens parameters, there are five quantile values to choose,
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
    - Only ens parameters can use quantiles option.

The output of this command is a `html` video file which means it can be opened in the web browser. 

!!! info
    The lead days for `hres` is 10 days while for `ens` is 15 days.