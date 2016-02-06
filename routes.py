from apis import LoginAPI, UserAPI, CategoryAPI, PersonAPI


def register_api(app, view, endpoint, url, pk, pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule('/api/{}/<int:user_id>/'.format(url), defaults={pk: None},
                     view_func=view_func, methods=['GET', ])
    app.add_url_rule('/api/{}/<int:user_id>/'.format(url), view_func=view_func, methods=['POST', ])
    app.add_url_rule('/api/{}/<int:user_id>/<{}:{}>'.format(url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])


def init_app(app):
    user_view = UserAPI.as_view('user_api')
    app.add_url_rule('/api/users/', view_func=user_view, methods=['POST', ])
    app.add_url_rule('/api/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])

    login_view = LoginAPI.as_view('login_api')
    app.add_url_rule('/api/login/', view_func=login_view, methods=['POST', ])

    register_api(app, CategoryAPI, 'category_api', 'categories', 'category_id')
    register_api(app, PersonAPI, 'person_api', 'people', 'person_id')
