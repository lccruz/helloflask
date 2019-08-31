from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    message = "Flask and you"
    return jsonify({"message": message}), 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
