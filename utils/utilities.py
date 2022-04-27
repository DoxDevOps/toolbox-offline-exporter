# coding=utf-8

""" These are universal functions that do not depend on any other function/ functionality of toolbox"""
import json


def load_file(location):
    """
    a function that loads a json file
    :type location: string
    :return: json object
    """
    with open(location) as f:
        data = json.load(f)
    return data


def write_file(location, info):
    """
    function that writes to a json file
    :param location: where the json file is located
    :param info: info to write to json file
    :return:  boolean (just a checker)
    """
    with open(location, "w") as data:
        data.write(json.dumps(info))
        data.close()
    return True
