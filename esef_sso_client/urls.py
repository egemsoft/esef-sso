from django.conf.urls import patterns, include, url

# -*- coding: utf-8 -*-
from esef_client import SSO_CLIENT_REQUIRED, sso_client


urlpatterns = patterns('')

if SSO_CLIENT_REQUIRED:
    urlpatterns += patterns(
        url(r'^login/', include(sso_client.get_urls())),
    )
