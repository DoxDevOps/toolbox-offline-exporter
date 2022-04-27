# coding=utf-8
import json


def validate_config_file():
    """
    validates if data is in the correct format
    :return: Return False when the file is not correct
    """
    try:
        with open('config/config.json') as f:
            return json.load(f)
    except ValueError as e:
        return False


def save_facility_details(site_data):  # this function will be called whe we implement a POP UP MENU for Site
    """
    gets facility details as dictionary and saves the file as a json file
    :param site_data:
    :return:
    """
    # details to be entered on the web browser
    if site_data["apps"][0] == "Point of Care":
        app_id = 1
    else:
        app_id = 2

    site_name = site_data["name"]
    uuid = site_data["uuid"]
    with open("config/config.json", "w") as data:
        information = {"uuid": uuid, "app_id": app_id, "site_name": site_name}
        data.write(json.dumps(information))
        data.close()
    return True
