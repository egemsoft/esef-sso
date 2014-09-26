from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


__author__ = 'ahmetdal'


class EsefSSOUser(AbstractUser):
    class Meta:
        app_label = 'esef_sso_client'

    access_token = models.CharField(_('Last Access Token'), max_length=200, null=True, blank=True)


    def is_authenticated(self):
        from esef_sso_client import sso_client

        return sso_client.is_authenticated(self)


