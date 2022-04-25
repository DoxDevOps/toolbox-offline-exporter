#! /usr/bin/python
import getpass
import json
import os

import requests as requests
from flask import request


def configure_site():
    """user = getpass.getuser()
    #Configures the site
    # install pip
    print(" Step 1 : Update laptop")
    answer = os.system("sudo apt-get update")
    print("Step 2: Install Pip.")
    answer1 = os.system("sudo apt install python-pip")
    print(answer1)
    print("Step3 : install python environment")
    os.system("sudo apt install virtualenv")
    os.system("virtualenv flask")
    print("creating Toolbox Service")
    # here is the code for creating the site.

    os.system("sudo cp toolbox.service /etc/systemd/system/")
    os.system("sudo systemctl daemon-reload && sudo systemctl start toolbox && sudo systemctl enable toolbox")
    print("creating browser shortcut !!")
    os.system("cp toolbox.desktop /home/"+user+"/Desktop/")
    print("Set Up is COMPLETE !!!!!!!!!!!!!!!!!!!")"""
    response = requests.get(url="https://toolbox.hismalawi.org/ext-api/site/get/details", data=json.dumps({"site_name":"DHO"}),
                            headers={"Content-type": "application/json", "Accept": "text/plain",
                                     "Authorization": "yyJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2MzY0MjQ0NjR9.iRlIMoZgYUQxZMq-CZiLusUfPyofkLCA8djNbOaJYT0"})
    print(response.json())

    return True


def main():
    configure_site()
    return True


if __name__ == '__main__':
    main()
