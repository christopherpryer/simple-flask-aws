import os
import urllib3

root_dir = os.path.dirname(os.path.abspath(__name__))
instance_dir = os.path.join(root_dir, 'instance')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(instance_dir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=0
