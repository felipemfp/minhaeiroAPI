from flask import request, json
from helpers import Crypt, Auth
from flask.views import MethodView
from models import db, User, Category, Person, Transaction, TransactionItem


class UserAPI(MethodView):
    def get(self, user_id):
        auth_key = request.args.get('key')
        user = User.authenticate(user_id, auth_key)
        if user:
            return json.jsonify(user.as_dict())
        return json.jsonify({})

    def post(self):
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

    def user_put(self, user_id):
        auth_key = request.args.get('key')
        user = User.authenticate(user_id, auth_key)
        if user:
            new_user = request.get_json(force=True)
            user.name = new_user['name']
            user.login = new_user['login']
            user.password = Crypt.hash_sha256(new_user['password'])
            db.session.commit()
            return json.jsonify(user.as_dict())
        return json.jsonify({})

    def delete(self, user_id):
        auth_key = request.args.get('key')
        user = User.authenticate(user_id, auth_key)
        if user:
            db.session.delete(user)
            db.session.commit()
            return json.jsonify(user.as_dict())
        return json.jsonify({})


class LoginAPI(MethodView):
    def post(self):
        supposed_user = request.get_json(force=True)
        user = User.query.filter_by(login=supposed_user['login']).first()
        if user and user.password == Crypt.hash_sha256(supposed_user['password']):
            return json.jsonify(user.as_dict())
        return json.jsonify({})