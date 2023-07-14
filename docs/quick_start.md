In this section, we are going to set up a python virtual environment to use the dataex client. However, it should be noted that this step is not necessary to use dataex API.


## Virtual environment

If you want to isolate the environment for the DataEx client library from your system wide environment, then using a python virtual environment is the best way going forward.

### Installing the module

There are many modules which can be used for setting up a python virutal environment such as anaconda, virtualenv, pyenv etc. Using them is mostly straight forward. We can't go into detail of each module since it is beyond this documentation's scope. If you wanted to use the `virtualenv` module then installing it would be done by the following command,


```
$ pip install virtualenv
```
But with Python 3, you should already have the built-in `venv` module from python the standard library.

### Creating a virtual environment using venv

```
$ python3 -m venv env
```
The "env" is the name of the virtual environment. You can change it according to your preference. 

In order to use the environment, you have to activate it. 

```
$ source env/bin/activate

(env) $
``` 
The env within the parenthesis is the name of the environment. It's apperance means that you are now inside the virtual environment.

If you need to exit the virtual environment then just type deactivate and press enter.
```
(env) $ deactivate

$
```
With this your shell prompt reverts to normal i.e without the parenthesized venv and the python executable now referring to the global python installation.

## Installation

```
pip install https://github.com/nzahasan/dataex-client/zipball/master
```

Finally, after running the above `pip` install command while the virtual environment is activated, we created an isolated python context that is not going to affect your global python setting.

### Running a command

```
(env)$ dataex_obs_data_summary.py --output_format csv --output ./summary.csv
```
There is no difference in the way a command is used. But now you have the advantage of running it inside its own isolated environment.
