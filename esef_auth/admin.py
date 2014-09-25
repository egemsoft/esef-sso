from django.contrib import admin
from guardian.models import UserObjectPermission

__author__ = 'ahmetdal'


class UserObjectPermissionAdmin(admin.ModelAdmin):
    change_list_template = 'admin/esef_auth_change_list.html'

    pass


admin.site.register(UserObjectPermission, UserObjectPermissionAdmin)
