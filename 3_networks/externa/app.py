# app.py
from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    data = requests.get('https://randomuser.me/api').json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)