from apis import LoginAPI, UserAPI, CategoryAPI, PersonAPI


def init_app(app):
    user_view = UserAPI.as_view('user_api')
    app.add_url_rule('/api/users/', view_func=user_view, methods=['POST', ])
    app.add_url_rule('/api/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])

    login_view = LoginAPI.as_view('login_api')
    app.add_url_rule('/api/login/', view_func=login_view, methods=['POST', ])

    category_view = CategoryAPI.as_view('category_api')
    app.add_url_rule('/api/categories/<int:user_id>/', defaults={'category_id': None},
                     view_func=category_view, methods=['GET', ])
    app.add_url_rule('/api/categories/<int:user_id>/', view_func=category_view, methods=['POST', ])
    app.add_url_rule('/api/categories/<int:user_id>/<int:category_id>',
                     view_func=category_view, methods=['GET', 'PUT', 'DELETE'])

    person_view = PersonAPI.as_view('person_api')
    app.add_url_rule('/api/people/<int:user_id>/', defaults={'person_id': None},
                     view_func=person_view, methods=['GET', ])
    app.add_url_rule('/api/people/<int:user_id>/', view_func=person_view, methods=['POST', ])
    app.add_url_rule('/api/people/<int:user_id>/<int:person_id>',
                     view_func=person_view, methods=['GET', 'PUT', 'DELETE'])
