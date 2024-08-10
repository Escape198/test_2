from flask_appbuilder.security.manager import AUTH_DB, AUTH_OAUTH
import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    AUTH_TYPE = AUTH_DB

    OAUTH_PROVIDERS = [{
        'name': 'github',
        'icon': 'fa-github',
        'token_key': 'access_token',
        'remote_app': {
            'consumer_key': os.getenv('GITHUB_CLIENT_ID'),
            'consumer_secret': os.getenv('GITHUB_CLIENT_SECRET'),
            'request_token_params': {
                'scope': 'email'
            },
            'base_url': os.getenv('VENDOR_GITHUB_API'),
            'request_token_url': None,
            'access_token_url': os.getenv('VENDOR_GITHUB_AUTH') + '/access_token',
            'authorize_url': os.getenv('VENDOR_GITHUB_AUTH') + '/authorize',
        }
    }]

    AUTH_USER_REGISTRATION = True
    AUTH_USER_REGISTRATION_ROLE = 'Admin'
