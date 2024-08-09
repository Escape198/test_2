from flask_appbuilder import ModelView
from app.models import User
from app import appbuilder, db


class UserView(ModelView):
    datamodel = SQLAInterface(User)
    list_columns = ['field1', 'field2']


appbuilder.add_view(MyModelView, "User", icon="fa-folder-open-o", category="Category")
