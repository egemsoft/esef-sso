from __future__ import unicode_literals


class ConsumerAccessPermissionBackend(object):
    supports_object_permissions = True
    supports_anonymous_user = True
    supports_inactive_user = True

    def authenticate(self, username, password):
        return None

    def has_perm(self, user_obj, perm, obj=None):
        from esef_sso_client import SSO_CLIENT_REQUIRED, sso_client

        if SSO_CLIENT_REQUIRED:
            if not sso_client.get_user(user_obj.access_token):
                return False
        else:
            return True

