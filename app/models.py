from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String


class User(Model):
    id = Column(Integer, primary_key=True)
    field1 = Column(String(150), nullable=False)
    field2 = Column(String(150), nullable=False)

    def __repr__(self):
        return self.field1
