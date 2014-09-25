from django.db import models

from django.db.models.base import ModelBase

from esef_auth.models.managers.filtered_model_manager import FilteredModelManager

from esef_auth.utils.registry import Registry


__author__ = 'ahmetdal'

filtered_class_registry = Registry()


class FilteredModelMetaclass(ModelBase):
    def __new__(cls, name, bases, attrs):
        result = super(FilteredModelMetaclass, cls).__new__(cls, name, bases, attrs)
        filtered_class_registry.register('name', result)
        return result


class FilteredModel(models.Model):
    __metaclass__ = FilteredModelMetaclass

    class Meta:
        abstract = True

    objects = FilteredModelManager()
