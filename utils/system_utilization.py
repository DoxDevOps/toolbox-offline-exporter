import platform
import subprocess
import json
import psutil
from psutil._common import bytes2human

ram = psutil.virtual_memory()
disk_space = psutil.disk_usage('/')


def get_ram_details():
    ram_dict = \
        {
            "total": bytes2human(ram.total),
            "used": bytes2human(ram.used),
            "free": bytes2human(ram.free),
            "percentage": int(ram.percent)

        }
    json_object = json.dumps(ram_dict)

    return json_object


def get_hdd_details():
    hdd_dict = \
        {
            "total": disk_space.total,
            "used": disk_space.used,
            "free": disk_space.free,
            "percentage": int(disk_space.percent)
        }
    json_object = json.dumps(hdd_dict)

    return json_object


def check_service():
    services = ["docker", "mysql", "nginx"]  # service to check (Active or Inactive)
    running_services_dict = {}
    for service in services:
        p = subprocess.Popen(["systemctl", "is-active", service], stdout=subprocess.PIPE)
        (output, err) = p.communicate()
        output = output.decode('utf-8')
        running_services_dict[service] = output

    json_object = json.dumps(running_services_dict)

    return json_object


def platform_info():
    osname = platform.system()
    version = platform.release()
    osname = osname.split('\n')
    version = version.split('\n')
    for x in version:
        version_str = x.strip()
    for y in osname:
        osname_str = y.strip()
    #encrypt.encrypt_data("OS release", version_str)
    #encrypt.encrypt_data("OS", osname_str)
