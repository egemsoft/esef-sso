from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


__author__ = 'ahmetdal'


class EsefUser(get_user_model()):
    class Meta:
        app_label = 'esef'

    access_token = models.CharField(_('Last Access Token'), max_length=200, null=True, blank=True)


