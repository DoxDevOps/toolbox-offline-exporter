
import json
from flask import Flask, render_template
from utils.export_emr_data import check_systems
from utils.generate_qr_image import add_qr_data
from utils.validate_emr_data import validate_config_file

app = Flask(__name__, static_folder="templates/static")


@app.route('/toolbox')
def extract_data():
    """gets EMR data and creates a QR Image
    Args: None
    Returns:
        dict: hosts from api
    """
    # first verify if the data is correct in the config file
    config_file_data = validate_config_file()
    if not config_file_data:
        configure_toolbox()
    # if all is alright, then do the following
    # 1. get EMR version
    emr_data = check_systems()
    if not emr_data:
        return False
    # 2. This is a final Dictionary to be sent for QR Image generation
    final_emr_data = \
        {
            "1": "Toolbox",
            "uuid": config_file_data["uuid"],
            "app_id": config_file_data["app_id"],
            "module": emr_data

        }

    final_string_to_decrypt = json.dumps(final_emr_data)
    # 3. Add the data to QR Image
    add_qr_data(final_string_to_decrypt)

    # 4 Get facility name . This name will be displayed on UI
    with open('config/config.json') as f:
        site_name = json.load(f)
        print(site_name["site_name"])
    return render_template('index.html', site_name=site_name["site_name"])


@app.route('/setup')
def configure_toolbox():
    """
    Console Functionality that enables a user to configure toolbox
    Args: None
    Returns:

    """
    return True


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=6010)
