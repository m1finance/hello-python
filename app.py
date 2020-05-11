from flask import Flask, jsonify
import json, os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify(dict(os.environ))

@app.route('/env')
def return_env():
    return jsonify(dict(os.environ))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')