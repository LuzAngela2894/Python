from flask import Flask, request, jsonify
from config import config
from models import db, User


def create_app(environment):
    app = Flask(__name__)

    app.config.from_object(environment)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app


environment = config['development']
app = create_app(environment)


@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = [user.json() for user in User.query.all()]
    return jsonify({'users': users})


@app.route('/api/v1/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify({'message': 'User does not exists'}), 404

    return jsonify({'user': user.json()})


@app.route('/api/v1/users/', methods=['POST'])
def create_user():
    json = request.get_json(force=True)
    if json.get('username') is None:
        return jsonify({'message': 'Bad request'}), 400

    user = User.create(json['username'])

    return jsonify({'user': user.json()})


@app.route('/api/v1/users/<id>', methods=['PUT'])
def update_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify({'message': 'User does not exists'}), 404

    json = request.get_json(force=True)
    if json.get('username') is None:
        return jsonify({'message': 'Bad request'}), 400

    user.username = json['username']

    user.update()

    return jsonify({'user': user.json()})


@app.route('/api/v1/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return jsonify({'message': 'User does not exists'}), 404

    user.delete()
    return jsonify({'user': user.json()})


if __name__ == '__main__':
    app.run(host="localhost", port=6060, debug=True)
