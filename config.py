import os
basedir = os.path.abspath(os.path.dirname(__file__))

#config class that defines secret_key for form protection
#SQLALCHEMY_DATABASE_URI holds location of DB
#SQLALCHEMY_TRACK_MODIFICATIONS is turned off
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
