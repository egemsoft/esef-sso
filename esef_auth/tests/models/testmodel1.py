from django.db import models

from esef_auth.models.filtered_model import FilteredModel


__author__ = 'ahmetdal'


class TestModel1(FilteredModel):
    class Meta:
        db_table = "test_model1"
        app_label = "tests"

    field = models.CharField(max_length=50, null=True, blank=True)
