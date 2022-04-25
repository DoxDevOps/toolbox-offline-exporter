import json
from flask import Flask, render_template, request

app = Flask(__name__, static_folder="templates/static")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=6070)


@app.route('/toolbox')
def extract_data():
    """gets EMR data and creates a QR Image
    Args: None
    Returns:
        dict: hosts from api
    """
    return 1


@app.route('/setup')
def configure_toolbox():
    """gets EMR data and creates a QR Image
    Args: None
    Returns:
        dict: hosts from api
    """
    return 1
