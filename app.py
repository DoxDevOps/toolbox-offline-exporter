import json
from flask import Flask, render_template, request

app = Flask(__name__, static_folder="templates/static")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=6070)
