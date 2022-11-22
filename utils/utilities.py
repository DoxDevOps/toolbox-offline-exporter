# coding=utf-8

""" These are universal functions that do not depend on any other function/ functionality of toolbox"""
import json
import urllib2


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


def get_request(url, token, body):
    """
    makes a get request based on keywords sent from the body
    :param url: endpoint
    :param token: for authorization
    :param body: data to be sent to the endpoint
    :return: info from the endpoint
    """
    req = urllib2.Request(url, body)
    req.get_method = lambda: 'GET'
    req.add_header('Content-type', 'application/json')
    req.add_header('Accept', 'text/plain')
    req.add_header('Authorization', token)
    r = urllib2.urlopen(req)
    results = r.read()
    return results

def get_host_pass():
    """
    a function that read password stored in a file
    :return: passwrd as str
    """
    file = open("../config/___rapt___.txt","r")
    passwrd = file.read()
    file.close()
    return passwrd.strip()

def save_host_pass(passwrd):
    """
    a function that stores password in a file
    :param passwrd: passwrd to be stored
    :return: passwrd as str
    """
    file = open("../config/___rapt___.txt","w")
    file.write(passwrd.strip())
    file.close()
    return passwrd.strip()
