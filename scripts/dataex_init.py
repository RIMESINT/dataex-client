import os
import getpass
import json


def main():
        home_dir = os.environ['HOME']
        username = input("Enter your dataex username:")
        password = getpass.getpass(prompt="Enter your password:")
        auth_json = {}
        auth_json['username'] = username
        auth_json['password'] = password
        auth_json['token'] = ''

        with open(f'{home_dir}/.dataex_auth.json','w') as f:
            json.dump(auth_json, f)



if __name__=='__main__':
    main()