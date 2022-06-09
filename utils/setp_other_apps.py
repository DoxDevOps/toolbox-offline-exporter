# coding=utf-8
import json

from utils.validate_emr_data import append_other_apps


def choose_app():
    print("Please select other apps installed !")
    print("1. NONE \n 2. ANC \n 3. Maternity \n 4. HTS \n 5. OPD \n 6. CRVS \n 7. Lab Ordering System")
    app_name = raw_input("Enter your Selection number: ")
    check_chosen_app(app_name)
    return True

def check_chosen_app(app_id):
    while True:
        try:
            if app_id > 7:
                print("The number selected is not on the list, Please try again.")
                continue
            if app_id < 0:
                print("Please Select a POSITIVE number")
                continue
            if app_id == 1:
                break
            append_other_apps(site_data)
        except ValueError:
            print("\nPlease enter a valid number")
            continue
        else:
            break