from flask import Flask, send_from_directory
from sys_monitor import getTemps
from flask import jsonify
import random

app = Flask(__name__)

@app.route("/")
def base():
    return send_from_directory('client/public', 'index.html')

@app.route("/<path:path>")
def home(path):
    return send_from_directory('client/public', path)

@app.route("/sys_stats/", methods=['GET'])
def sys_stats():
    response = jsonify(getTemps())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)