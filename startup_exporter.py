import json
import requests
from config.config import data, setup_emr, bridge_endpoint
from utils.export_emr_data import  get_emr_version 
from utils.validate_emr_data import validate_config_file

def collect_and_send():
    if not validate_config_file(data["config"]) or not validate_config_file(data["apps_loc"]):
        return

    
    emc_data = setup_emr["emc"]
    emr_data = get_emr_version(emc_data)
    config_file_data = validate_config_file(data["config"])
    uuid = config_file_data["uuid"]
    
    final_emr_data = {
        "uuid": uuid,
        "app_dir": emc_data,
        "version": emr_data
    }

    print(final_emr_data)
    # Send to endpoint
    
    try:
        response = requests.post(bridge_endpoint, json=final_emr_data)
        print("Status:", response.status_code)
    except Exception as e:
        print("Failed to send data:", e)

if __name__ == "__main__":
    collect_and_send()



