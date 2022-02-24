## Check System States CLI

This script allows to view the information on available parameters for a specific system state.


###Usage
```
$ dataex_check_system_state.py --state_name <str> --output <str>
```

This will download a json file related to the desired system state's information on available parameters. 

###Example

```
$ python dataex_check_system_state.py --state_name ECMWF_HRES_NC --output $HOME/system_state_params.json
```
