## Get parameters for forecast graphics CLI

The forecast graphics engine provides single or animated graphs for three model types - ECMWF HRES, ECMWF ENS & ECMWF SEAS. This command helps to find the parameters which are available for these three models. After obtaining the parameter names, you can use them to download graphs or animation with `dataex_forecast_graph.py` or `dataex_forecast_animation.py` commands respectively.

###Usage
```
$ dataex_forecast_graph_params.py --model_type <str>
```

Running this command will print a table in terminal containing the parameters for the desired model type.

###Example
```
dataex_forecast_graph_params.py -mt ecmwf_seas

```
