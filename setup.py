#! /usr/bin/python3
import os

from utils.setup_toolbox import mac_address, get_facility_name
from utils.setup_toolbox import get_serial

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
    # os.system("sudo apt install python3-pip")
    os.system("python3 -m pip install --user --upgrade pip")
    #os.system("python3 -m venv flask3")
    # if flask3 environment is already ther, delete it first
    if os.path.exists("flask3"):
        os.system("rm -rf flask3")

    print("Step 3: Create Virtual Environment")
    os.system("python3 -m venv flask3")
    print("*********** SETTING FACILITY DETAILS *****************")
    os.system(". flask3/bin/activate && sudo apt install -y libjpeg-dev zlib1g-dev libfreetype6-dev liblcms2-dev libopenjp2-7-dev libtiff5-dev tk-dev tcl-dev")
    os.system(". flask3/bin/activate && pip install --upgrade pip setuptools wheel")
    
    os.system(". flask3/bin/activate && pip3 install -r requirements.txt && sudo apt-get install git")

    print("******************************************************")
    
    os.system(". flask3/bin/activate && python3 -c 'from utils.setup_toolbox import "
              "get_facility_name; "
              "get_facility_name()'")
    mac_address()
    # get system serial number
    get_serial()
    print("*********** END - Facility Configured Successfully *****************")
    print("creating Toolbox Service")
    os.system("sudo cp toolbox.desktop ~/Desktop/")
    # here is the code for creating the site.
    os.system("sudo cp toolbox.service /etc/systemd/system/")
    os.system("sudo systemctl daemon-reload && sudo systemctl start toolbox && sudo systemctl enable toolbox")
    print("FINISHED :creating Toolbox Service \n")
    print("Now Creating  toolbox start app service")
    print("This process will take a few minutes, please wait...")
    os.system("sudo cp toolbox-startup.service /etc/systemd/system/")
    os.system("sudo systemctl daemon-reload && sudo systemctl start toolbox-startup && "
              "sudo systemctl enable toolbox-startup")
    print("FINISHED :creating toolbox start app service \n")
    print("******************************************************************** \n")
    print("Now lets create a timer for our service to start after 15 minutes ")
    os.system("sudo cp toolbox-startup.timer /etc/systemd/system/")
    os.system("sudo systemctl daemon-reload && sudo systemctl start toolbox-startup.timer && "
              "sudo systemctl enable --now toolbox-startup.timer")    

    print("FINISHED :creating timer for toolbox start app service \n")
    print("Step 4: Setting up other modules")
    print("Lastly select other modules installed !")
    os.system(". flask3/bin/activate && python3 -c 'from utils.setup_other_apps import "
              "choose_app; "
              "choose_app()'")
    print("FINISHED :Setting up other modules")
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
