from flask import Flask, render_template
from flask import jsonify
from db import db
from models import ArtistModel


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.route('/')
def hello_world():
    message = "Flask 3000"
    return jsonify({"message": message}), 200


@app.route('/<message>')
def hello_message(message):
    return render_template('index.html', message=message)


@app.route('/artists/')
def list_artists():
    artists = ArtistModel.find_all()
    return render_template('list_artists.html', artists=artists)


if __name__ == '__main__':
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.drop_all()
        db.create_all()
        luciano = ArtistModel(name="Luciano")
        luciano.save_to_db()
        fabiana = ArtistModel(name="Fabiana")
        fabiana.save_to_db()

    app.run(host='127.0.0.1', port='5000', debug=True)
