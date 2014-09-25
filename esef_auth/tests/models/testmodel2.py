from django.db import models

from esef_auth.models.filtered_model import FilteredModel
from esef_auth.tests.models import TestModel1


__author__ = 'ahmetdal'


class TestModel2(FilteredModel):
    class Meta:
        db_table = "test_model2"
        app_label = "tests"

    field = models.CharField(max_length=50, null=True, blank=True)

    test_model1 = models.ForeignKey(TestModel1)