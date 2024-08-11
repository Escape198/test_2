import os
from flask_appbuilder.security.manager import AUTH_OAUTH, AUTH_DB
from pathlib import Path
from secrets import token_urlsafe
from urllib.parse import urljoin


BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = os.getenv('SECRET_KEY', token_urlsafe(24))
VENDOR_GITHUB_AUTH = os.getenv('VENDOR_GITHUB_AUTH', 'https://github.com/login/oauth')
VENDOR_GITHUB_API = os.getenv('VENDOR_GITHUB_API', 'https://api.github.com/')
SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR / 'app.db'}"
SQLALCHEMY_TRACK_MODIFICATIONS = False

FAB_API_SWAGGER_UI = True
AUTH_TYPE = AUTH_DB if os.getenv('AUTH_TYPE', 'AUTH_DB') == 'AUTH_DB' else AUTH_OAUTH

OAUTH_PROVIDERS = [{
    'name': 'github',
    'token_key': 'access_token',
    'icon': 'fa-github',
    'remote_app': {
        'client_id': os.getenv('GITHUB_CLIENT_ID'),
        'client_secret': os.getenv('GITHUB_CLIENT_SECRET'),
        'api_base_url': VENDOR_GITHUB_API,
        'request_token_url': None,
        'access_token_url': urljoin(VENDOR_GITHUB_AUTH, '/access_token'),
        'authorize_url': urljoin(VENDOR_GITHUB_AUTH, '/authorize'),
        'client_kwargs': {
            'scope': 'user:email',
        }
    }
}]
