from flask import Flask, request, json
from models import *
from helpers import *

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

db.init_app(app)

@app.route('/api')
def api():
    return '<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>'


@app.route('/api/login', methods=['POST'])
def login():
    supposed_user = request.get_json(force=True)
    user = User.query.filter_by(login=supposed_user['login']).first()
    if user and user.password == Crypt.hash_sha256(supposed_user['password']):
        return json.jsonify(user.as_dict())
    return json.jsonify({})


@app.route('/api/<auth_key>/user/<user_id>', methods=['GET'])
def user_get(auth_key, user_id):
    user = User.authenticate(user_id, auth_key)
    if user:
        return json.jsonify(user.as_dict())
    return json.jsonify({})


@app.route('/api/user', methods=['POST'])
def user_post():
    supposed_user = request.get_json(force=True)
    if supposed_user:
        user = User()
        user.name = supposed_user['name']
        user.login = supposed_user['login']
        user.password = Crypt.hash_sha256(supposed_user['password'])
        user.auth_key = Auth.get_new_key()
        db.session.add(user)
        db.session.commit()
        if user.user_id:
            return json.jsonify(user.as_dict())
    return json.jsonify({})


@app.route('/api/<auth_key>/user/<user_id>', methods=['PUT'])
def user_put(auth_key, user_id):
    user = User.authenticate(user_id, auth_key)
    if user:
        new_user = request.get_json(force=True)
        user.name = new_user['name']
        user.login = new_user['login']
        user.password = Crypt.hash_sha256(new_user['password'])
        db.session.commit()
        return json.jsonify(user.as_dict())
    return json.jsonify({})


@app.route('/api/<auth_key>/user/<user_id>', methods=['DELETE'])
def user_delete(auth_key, user_id):
    user = User.authenticate(user_id, auth_key)
    if user:
        db.session.delete(user)
        db.session.commit()
        return json.jsonify(user.as_dict())
    return json.jsonify({})


if __name__ == '__main__':
    app.run()