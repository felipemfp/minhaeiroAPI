from apis import LoginAPI, UserAPI


def init_app(app):
    user_view = UserAPI.as_view('user_api')
    app.add_url_rule('/api/user/', view_func=user_view, methods=['POST', ])
    app.add_url_rule('/api/user/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])

    login_view = LoginAPI.as_view('login_api')
    app.add_url_rule('/api/login/', view_func=login_view, methods=['POST', ])
