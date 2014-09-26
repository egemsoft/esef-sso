# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin

from esef_sso_server import sso_server


urlpatterns = patterns('',
                       url('', include('django.contrib.auth.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^server/', include(sso_server.get_urls())),
)