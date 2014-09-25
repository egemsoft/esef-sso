from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext_lazy as _


__author__ = 'ahmetdal'


class EsefSSOUser(User):
    class Meta:
        app_label = 'esef_sso_client'

    access_token = models.CharField(_('Last Access Token'), max_length=200, null=True, blank=True)


