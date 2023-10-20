import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(dict(message='hello'))
