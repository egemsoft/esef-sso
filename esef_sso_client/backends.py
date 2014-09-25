from __future__ import unicode_literals
from esef_client import SSO_CLIENT_REQUIRED, sso_client


class ConsumerAccessPermissionBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = True
    supports_inactive_user = True

    def authenticate(self, username, password):
        return None

    def has_perm(self, user_obj, perm, obj=None):


        if SSO_CLIENT_REQUIRED:
            if not sso_client.get_user(user_obj.access_token):
                return False
        else:
            return True

