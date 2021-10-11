## Create dataex auth file CLI

It is a script to be used for creating the `.dataex_auth.json` file. The user is prompted to enter dataex username and password in the terminal after running this command.

##Usage

```
$ dataex_init.py
```

Executing this command creates a hidden file that is stored in the home directory which will be used for authentication. The user must already have a registered dataex account. To avoid rejection, users must first visit the website and then create a dataex user account. 

However, not running this command in the beginning will not impede the usage of other scripts. This is possible because of `auth` module which also creates the authentication file if one is not already present.
