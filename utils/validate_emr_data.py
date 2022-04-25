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