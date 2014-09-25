from django.conf import settings
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.db import models
from guardian.models import UserObjectPermission
from esef_auth.utils import middleware


__author__ = 'ahmetdal'

get_current_user = getattr(settings, 'GET_CURRENT_USER') if hasattr(settings, 'GET_CURRENT_USER') else middleware.get_user


class FilteredModelManager(models.Manager):
    user_owned_objects_field = 'user'

    class Meta:
        abstract = True


    def filter(self, *args, **kwargs):
        data_filter_on = kwargs.pop('data_filter_on', None)
        qs = super(FilteredModelManager, self).filter(*args, **kwargs)
        if data_filter_on is not None:
            field_names = data_filter_on.split('__') if data_filter_on is not '' else []
            model = self.model
            for field_name in field_names:
                field = model._meta.get_field_by_name(field_name)[0]
                if hasattr(field, 'rel') and hasattr(field.rel, 'to'):
                    model = field.rel.to
                else:
                    raise Exception('%s part does not present a related field')

            content_type = ContentType.objects.get_for_model(model)
            current_user = get_current_user()
            permission = Permission.objects.get(content_type=content_type, codename='change_%s' % model._meta.module_name)
            permitted_object_ids = UserObjectPermission.objects.filter(user=current_user, content_type=content_type, permission=permission).values_list('object_pk', flat=True)

            key = '%s__pk__in' % data_filter_on if data_filter_on is not '' else 'pk__in'
            filters = {key: permitted_object_ids}
            qs = qs.filter(**filters)
        return qs


