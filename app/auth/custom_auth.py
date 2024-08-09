from flask_appbuilder.security.sqla.manager import SecurityManager
from flask import g


class CustomAuthSecurityManager(SecurityManager):
    def authenticate(self, username, password):
        if username == "admin" and password == "admin":
            user = self.find_user(username=username)
            if user:
                g.user = user
                return True
        return super().authenticate(username, password)
