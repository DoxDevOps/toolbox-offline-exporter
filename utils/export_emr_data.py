# coding=utf-8
import subprocess
from os.path import exists
from flask import json

from utils.utils import load_file


def check_systems():
    """
    checks if EMR installation folders are available
    :return:
    """
    version_dict = {}
    apps_dir = load_file("config/apps.config")
    for each_dir_key, each_dir_value in apps_dir:
        if exists(each_dir_value):
            tag = get_emr_versions(each_dir_value)
            version_dict[each_dir_key] = tag

    json_object = json.dumps(version_dict)
    json_object = json.loads(json_object)
    return json_object


def get_emr_versions(each_dir_value):
    """
    get emr version from the installation folder
    :return:
        string: emr tags
    """
    emc_result = subprocess.Popen("git describe --tags", shell=True, cwd='{}'.format(each_dir_value), stdout=subprocess.PIPE)
    emc_result = emc_result.stdout.read().strip()
    return emc_result







