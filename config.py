import os

basedir = os.path.abspath(os.path.dirname(__file__))
class config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database/listapp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False