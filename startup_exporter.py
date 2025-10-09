import json
import requests
from config.config import data
from utils.export_emr_data import check_installation_folders, get_emr_versions 
from utils.validate_emr_data import validate_config_file

def collect_and_send():
    if not validate_config_file(data["config"]) or not validate_config_file(data["apps_loc"]):
        return

    emr_data = check_installation_folders(data["apps_loc"])
    emc_data = get_emr_versions(data["emc_loc"])    
    uuid = data["uuid"]

    final_emr_data = {
        "uuid": uuid,
        "app_dir": emr_data,
        "version": emc_data
    }

    # Send to endpoint
    endpoint = data["bridge_endpoint"]  # <-- change this to your endpoint
    try:
        response = requests.post(endpoint, json=final_emr_data)
        print("Status:", response.status_code)
    except Exception as e:
        print("Failed to send data:", e)

if __name__ == "__main__":
    collect_and_send()