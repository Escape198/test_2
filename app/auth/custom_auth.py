from flask_appbuilder.security.sqla.manager import SecurityManager
from flask import g, request


class CustomAuthSecurityManager(SecurityManager):
    def authenticate(self, username=None, password=None):
        if request.form and 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            user = self.find_user(username=username)
            if user and self._verify_password(password, user.password):
                g.user = user
                return True

        if not username and 'oauth_provider' in request.args:
            oauth_provider = request.args['oauth_provider']
            user = self.oauth_user_info()
            if user:
                g.user = self.find_user(email=user['email'])
                return True

        return False

    def oauth_user_info(self):
        provider = self.appbuilder.sm.oauth_remotes['github']
        me = provider.get('user')
        return me.json() if me.status == 200 else None
