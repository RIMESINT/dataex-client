## Get Country Info CLI

It can be used to retrieve information such as Id number related to a specific country or all countries available on Dataex. 

###Usage
```
$ dataex_list_country_info.py --country <str> --output_format <str> --output <str>
```
!!! Tip
    Option names too long, you can always use their short forms. Check using `--help`
    
Options:
```
output_format : str
                json, table or csv  

country       : str
                name of country      

output        : str
                output filename
```      
   
The default output format is `table`. Hence, leaving this option out from the command is not a problem. The `output` option is not required as well.

###Example

```
$ dataex_list_country_info.py --country Bangladesh --output_format  json --output ./country_info.json

```
Here, a json file with country information is downloaded.


```
$ dataex_list_country_info.py
```
All country data is downloaded and shown in tabular form.

```
$ dataex_list_country_info.py --country Nepal
```
This downloads and displays information on the terminal in `table` format for Nepal. 


!!! tip
    If country option is not provided then information on all countries in the dataex is downloaded which can be saved in an output file. 


