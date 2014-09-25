from django.conf.urls import patterns, include, url

# -*- coding: utf-8 -*-
from django.contrib import admin
from esef_auth.views.user_object_permission_bulk_create_view import UserObjectPermissionBulkCreateView

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^user_object_permission_bulk_create/', UserObjectPermissionBulkCreateView.as_view(), name='user_object_permission_bulk_create'),
)
