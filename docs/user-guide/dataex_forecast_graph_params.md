## Get parameters for forecast graphics CLI

The forecast graphics engine provides single or animated graphs for three model types - HRES, ENS & SEAS. This command helps to find the parameters which are available for these models. After getting the parameter names, you can use them to download graphs or animation with `dataex_forecast_graph.py` or `dataex_forecast_animation.py` commands respectively.

###Usage
```
$ dataex_forecast_graph_params.py --model_type <str>
```

Running this command will print a table in terminal containing the parameters for the desired model type.