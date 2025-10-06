import json
import requests
from config.config import data
from utils.export_emr_data import check_installation_folders
from utils.generate_qr_image import add_qr_data
from utils.setup_toolbox import mac_address, get_serial
from utils.system_utilization import get_ram_details, get_hdd_details, platform_info, get_cpu_utilization
from utils.utilities import load_file
from utils.validate_emr_data import validate_config_file
from utils.get_serial import get_host_serial

def collect_and_send():
    if not validate_config_file(data["config"]) or not validate_config_file(data["apps_loc"]):
        return

    emr_data = check_installation_folders(data["apps_loc"])
    mac = mac_address()
    serial_number = get_host_serial()
    hdd = get_hdd_details()
    ram = get_ram_details()
    os_info = platform_info()
    cpu = get_cpu_utilization()

    final_emr_data = {
        "1": "Toolbox",
        "uuid": validate_config_file(data["config"])["uuid"],
        "app_id": validate_config_file(data["config"])["app_id"],
        "system_utilization": {
            "hdd_total_storage": hdd["hdd_total_storage"],
            "hdd_used_storage": hdd["hdd_used_storage"],
            "hdd_remaining_storage": hdd["hdd_remaining_storage"],
            "hdd_used_in_percentiles": hdd["hdd_used_in_percentiles"],
            "total_ram": ram["total_ram"],
            "used_ram": ram["used_ram"],
            "remaining_ram": ram["remaining_ram"],
            "cpu_utilization": cpu,
            "os_name": os_info["name"],
            "os_version": os_info["version"]},
        "module": emr_data,
        "serial_number": serial_number
    }

    # Send to endpoint
    endpoint = "http://your-endpoint-url/api/receive"  # <-- change this to your endpoint
    try:
        response = requests.post(endpoint, json=final_emr_data)
        print("Status:", response.status_code)
    except Exception as e:
        print("Failed to send data:", e)

if __name__ == "__main__":
    collect_and_send()