#! /usr/bin/python
import os
from utils.setup_toolbox import mac_address


def configure_site():
    """
    configures toolbox
    :return:
    """
    # Configures the site
    # install pip
    print("Step 1 : Update laptop")
    answer = os.system("sudo apt-get update")
    print("Step 2: Install Pip.")
    answer1 = os.system("sudo apt install python-pip")
    print(answer1)
    print("Step3 : install python environment")
    os.system("sudo apt install virtualenv")
    os.system("virtualenv flask")
    print("*********** SETTING FACILITY DETAILS *****************")
    os.system(". flask/bin/activate && python -c 'import setup_facility_details;  "
              "setup_facility_details.get_facility_name()'")
    mac = mac_address()
    print(mac)
    print("*********** END - Facility Configured Successfully *****************")
    print("creating Toolbox Service")
    # here is the code for creating the site.
    os.system("sudo cp toolbox.service /etc/systemd/system/")
    os.system("sudo systemctl daemon-reload && sudo systemctl start toolbox && sudo systemctl enable toolbox")
    print("FINISHED :creating Toolbox Service")
    return True


def main():
    """
    startup function
    :return: boolean
    """
    configure_site()
    return True


if __name__ == '__main__':
    main()
