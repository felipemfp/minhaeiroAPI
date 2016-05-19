import os

DEBUG = True
SQLALCHEMY_DATABASE_URI = os.environ.get('MINHAEIRO_DB', 'sqlite:////tmp/dev.db')
