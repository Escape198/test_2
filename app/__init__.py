import os
from dotenv import load_dotenv

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_migrate import Migrate

from app.config import SQLALCHEMY_DATABASE_URI
from app.custom_security_manager import CustomSecurityManager

load_dotenv()

app = Flask(__name__)
app.config.from_object('app.config')


db = SQLA(app)
migrate = Migrate(app, db)

appbuilder = AppBuilder(app, db.session, security_manager_class=CustomSecurityManager)
