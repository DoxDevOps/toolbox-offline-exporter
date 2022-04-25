# coding=utf-8
import subprocess
from os.path import exists, isdir, getsize
from flask import json
import netifaces

_command_ = "git describe --tags"  # command to check the tags
_emc_dir_ = "/var/www/emastercard-upgrade-automation"  # EMC installation directory
_emc_dir2_ = "/emastercard-upgrade-automation"  # some sites have EMC in the Home directory.

_poc_api_dir_ = "/var/www/BHT-EMR-API"  # POC Api Folder
_poc_core_dir_ = "/var/www/BHT-Core"  # POC Core Folder
_poc_core_art_dir_ = "/var/www/BHT-Core/apps/ART"  # POC ART Folder'''


def check_systems():
    """
    checks if EMR installation folders are available
    :return:
    """

    if exists(_emc_dir_ or _emc_dir2_):
        # emc can be installed in two different folders as described in the variables above
        if exists(_emc_dir_):  # if emc is in this folder
            return get_emc_versions(_emc_dir_)  # got get EMC versions
        return get_emc_versions(_emc_dir2_)  # if not, it is in this folder
    elif exists(_poc_api_dir_):  # check if poc api, core, art folder exist
        if exists(_poc_core_art_dir_):
            if exists(_poc_core_dir_):
                return get_poc_versions()
    else:
        return False


def get_poc_versions():
    """
    gets POC tags in all the installation folders

    param one
    :return:
        json: a  json object containing POC tags
    """

    api_result = subprocess.Popen(_command_, shell=True, cwd='{}'.format(_poc_api_dir_), stdout=subprocess.PIPE)
    core_result = subprocess.Popen(_command_, shell=True, cwd='{}'.format(_poc_api_dir_), stdout=subprocess.PIPE)
    art_result = subprocess.Popen(_command_, shell=True, cwd='{}'.format(_poc_api_dir_), stdout=subprocess.PIPE)
    api_result = api_result.stdout.read().strip()
    core_result = core_result.stdout.read().strip()
    art_result = art_result.stdout.read().strip()

    poc_version_dict = \
        {
            "api": api_result,
            "core": core_result,
            "art": art_result
        }
    json_object = json.dumps(poc_version_dict)
    json_object = json.loads(json_object)
    return json_object

    # Get EMC information


def get_emc_versions(directory):
    """
    get emc version from the installation folder

    :return:
        json: a  json object containing POC tags
    """
    emc_result = subprocess.Popen(_command_, shell=True, cwd='{}'.format(directory), stdout=subprocess.PIPE)
    emc_result = emc_result.stdout.read().strip()

    emc_version_dict = \
        {
            "emc": emc_result
        }
    json_object = json.dumps(emc_version_dict)
    json_object = json.loads(json_object)
    return json_object







