from flask import Flask, request, g
from models import db

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)

db.init_app(app)


if __name__ == '__main__':
    app.run()