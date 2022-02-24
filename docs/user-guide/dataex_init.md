## Create dataex auth file CLI

It is a script for creating the `.dataex_auth.json` file. The user is prompted to enter their Dataex account username and password in the terminal after running this command.

###Usage

```
$ dataex_init.py
```

Executing this command creates a hidden file which is stored in the user's home directory to be used for authentication. The user must already have a registered dataex account. To avoid failure in this case, users must create a Dataex user account. 

!!! info
    However, not running this command in the beginning will not impede the usage of other scripts. This is possible because `auth` module can also create the authentication file if one is not 
    already present.
