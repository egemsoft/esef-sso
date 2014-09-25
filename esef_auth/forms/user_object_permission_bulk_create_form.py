from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from esef_auth.models.filtered_model import filtered_class_registry
from esef_auth.services.auth_service import AuthService


__author__ = 'ahmetdal'


class UserObjectPermissionBulkCreateForm(forms.Form):
    permissions = forms.ModelMultipleChoiceField(queryset=Permission.objects.all())
    users = forms.ModelMultipleChoiceField(queryset=get_user_model().objects.all())
    objects = forms.MultipleChoiceField()

    def __init__(self, *args, **kwargs):
        super(UserObjectPermissionBulkCreateForm, self).__init__(*args, **kwargs)
        self.fields['objects'].choices = []
        cts = []
        for name, model in filtered_class_registry:
            if not model._meta.abstract:
                ct = ContentType.objects.get_for_model(model)
                self.fields['objects'].choices += [('%s__%s' % (ct.pk, o.pk), '%s | %s | %s' % (model._meta.app_label, model.__name__, o.__unicode__())) for o in model.objects.all()]
                cts.append(ct)
        self.fields['permissions'].queryset = Permission.objects.filter(content_type__in=cts)

    def clean_objects(self):
        identifiers = self.cleaned_data['objects']
        objects = []
        for identifier in identifiers:
            ct_id, object_id = identifier.split('__')
            ct = ContentType.objects.get(pk=ct_id)
            model = ct.model_class()
            objects.append(model.objects.get(pk=object_id))

        return objects


    def save(self, *args, **kwargs):
        print 'Test'
        permissions = self.cleaned_data['permissions']
        objects = self.cleaned_data['objects']
        users = self.cleaned_data['users']
        return AuthService.register_bulk_user_object_permissions(users, objects, permissions)









