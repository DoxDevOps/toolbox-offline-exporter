# coding=utf-8
import subprocess
from os.path import exists
from flask import json

from utils.utilities import load_file


def check_systems(location):
    """
    checks if EMR installation folders are available
    :return:
    """
    version_dict = {}
    apps_dir = load_file(location)
    for key, value in apps_dir:
        if exists(value):
            tag = get_emr_versions(value)
            version_dict[key] = tag

    json_object = json.dumps(version_dict)
    json_object = json.loads(json_object)
    return json_object


def get_emr_versions(directory):
    """
    get emr version from the installation folder
    :return:
        string: emr tags
    """
    emc_result = subprocess.Popen("git describe --tags", shell=True, cwd='{}'.format(directory), stdout=subprocess.PIPE)
    emc_result = emc_result.stdout.read().strip()
    return emc_result







