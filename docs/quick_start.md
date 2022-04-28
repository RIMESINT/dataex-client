We are going to set up a vitual environment to use the dataex client.

## Installation

This is the quickest and easiest way to install the API. You can then start using the scripts right away.
```
pip install https://github.com/nzahasan/dataex-client/zipball/master
```

## Using a virtual environment

If you want to isolate the environment for the datex client module from your system wide environment, then using python virtual environment is the best way going forward.

### Installing python virtualenv

If you don't already have it then use the following command to install.

```
$ pip install virtualenv
```
But with Python 3, you should already have the venv module from the standard library installed.

### Creating a virtual environment

```
$ python3 -m venv env
```
On python 3.6 and above, this is the recommended way to go. The "env" is the name of the virtual environment. You can change it according to your preference. 

In order to use the environment, you have to activate it. 

```
$ source env/bin/activate

(env) $
``` 
The env within the parenthesis is the name of the environment. It's apperance means that you are now inside the virtual environment.

If you need to go back to the system context then just execute deactivate.
```
(env) $ deactivate

$
```
With this your shell session reverts to normal with python commands referring to the global python install.

Finally, run the above `pip` install command while activating the virtual environment to create an isolated python context that is not going to affect your global python setting.

### Running a command

```
(env)$ dataex_obs_data_summary.py --output_format csv --output ./summary.csv
```
There is no difference in the way a command is used. But now you have the advantage of running it inside its own isolated environment.  
