from flask_appbuilder.security.sqla.manager import SecurityManager
from werkzeug.security import generate_password_hash, check_password_hash


class CustomSecurityManager(SecurityManager):
    def auth_user_db(self, username, password):
        user = self.find_user(username=username)

        if not user:
            user = self.add_user(
                username=username,
                first_name="Anonymous",
                last_name="User",
                email="user@default.com",
                role=self.find_role("Admin"),
                password=generate_password_hash(password)
            )

        return user
