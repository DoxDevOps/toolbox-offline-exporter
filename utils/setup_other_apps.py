# coding=utf-8
import json

from utils.validate_emr_data import append_other_apps


def choose_app():
    """
    a function that prompts a ser to enter other apps installed at a facility
    :return:
    """
    print("Please select other apps installed !")
    print("1. NONE \n 2. ANC \n 3. Maternity \n 4. HTS \n 5. OPD \n 6. CRVS \n 7. Lab Ordering System")

    check_chosen_app()
    return True


def check_chosen_app():
    """
    checks for the digits entered by user if they are valid
    :param app_id:
    """
    while True:
        try:
            app_id = int(raw_input("Enter your Selection number: "))
            if app_id > 7:
                print("The number selected is not on the list, Please try again.")
                continue
            if app_id < 0:
                print("Please Select a POSITIVE number")
                continue
            if app_id == 1:
                break
            append_other_apps(app_id)
        except ValueError:
            print("\nPlease enter a valid number")
            continue
        else:
            break
