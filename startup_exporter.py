import json
import time
import requests
from config.config import data, setup_emr, bridge_endpoint
from utils.export_emr_data import get_emr_version
from utils.validate_emr_data import validate_config_file


def collect_and_send():
    if not validate_config_file(data["config"]) or not validate_config_file(data["apps_loc"]):
        print("Configuration files are invalid. Exiting.")
        return

    emc_data = setup_emr["emc"]
    emr_data = get_emr_version(emc_data)
    config_file_data = validate_config_file(data["config"])
    uuid = config_file_data.get("uuid")

    final_emr_data = {
        "uuid": uuid,
        "app_dir": emc_data,
        "version": emr_data
    }

    print("Prepared EMR data:", final_emr_data)
    print(f"Sending data to: {bridge_endpoint}")

    max_retries = 5
    delay_seconds = 5  # wait time between retries

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.post(bridge_endpoint, json=final_emr_data, timeout=10)
            print(f"Attempt {attempt}: Status code {response.status_code}")

            if response.ok:
                print("Data sent successfully!")
                break  # success — stop retrying
            else:
                print(f"Server responded with {response.status_code}: {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt}: Failed to send data - {e}")

        if attempt < max_retries:
            print(f"Retrying in {delay_seconds} seconds...")
            time.sleep(delay_seconds)
        else:
            print("All attempts failed. Proceeding without crashing.")


if __name__ == "__main__":
    collect_and_send()
