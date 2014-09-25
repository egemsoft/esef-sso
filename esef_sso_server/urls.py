# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from esef_sso_server import sso_server

urlpatterns = patterns('')

urlpatterns += patterns(
    url(r'^server/', include(sso_server.get_urls())),
)