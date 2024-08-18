import os
from dotenv import load_dotenv

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_migrate import Migrate
from app.custom_security_manager import CustomSecurityManager

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'thisismysecretkey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLA(app)
migrate = Migrate(app, db)
appbuilder = AppBuilder(app, db.session, security_manager_class=CustomSecurityManager)
