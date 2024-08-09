import os
from dotenv import load_dotenv
from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_migrate import Migrate

from app.config import Config
from app.auth.custom_auth import CustomAuthSecurityManager

load_dotenv()

app = Flask(__name__)
app.config.from_object(Config)

db = SQLA(app)
migrate = Migrate(app, db)

appbuilder = AppBuilder(app, session=db.session, security_manager_class=CustomAuthSecurityManager)
