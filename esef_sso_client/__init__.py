__author__ = 'ahmetdal'

from django.conf import settings

SSO_CLIENT_REQUIRED = settings.ESEF_SSO_CLIENT_REQUIRED if hasattr(settings, 'ESEF_SSO_CLIENT_REQUIRED') else False

if SSO_CLIENT_REQUIRED:
    from simple_sso.sso_client.client import Client

    if not hasattr(settings, 'SSO_SERVER'):
        raise Exception('SSO_SERVER must be defined in your settings if ESEF_SSO_REQUIRED is set to True')

    if not hasattr(settings, 'SSO_PUBLIC_KEY'):
        raise Exception('SSO_PUBLIC_KEY must be defined in your settings if ESEF_SSO_REQUIRED is set to True')

    if not hasattr(settings, 'SSO_PRIVATE_KEY'):
        raise Exception('SSO_PRIVATE_KEY must be defined in your settings if ESEF_SSO_REQUIRED is set to True')

    sso_client = Client(settings.SSO_SERVER, settings.SSO_PUBLIC_KEY, settings.SSO_PRIVATE_KEY)
