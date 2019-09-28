from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello_world():
    message = "Flask 3000"
    return jsonify({"message": message}), 200


@app.route('/<message>')
def hello_message(message):
    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)
