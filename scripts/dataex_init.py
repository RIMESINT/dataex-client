#!/usr/bin/env python3

import os
import getpass
import json

from dataexclient.auth import auth


def main():
    auth_obj = auth()
    auth_obj.get_new_token_from_dataex()


if __name__ == '__main__':
    main()
