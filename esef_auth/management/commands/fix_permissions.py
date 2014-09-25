from django.db.models.loading import get_models

__author__ = 'ahmetdal'

from __future__ import unicode_literals, absolute_import, division

import sys

from django.conf import settings
from django.contrib.auth.management import _get_all_permissions
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.utils.encoding import smart_unicode


class Command(BaseCommand):
    help = "Fix permissions for proxy models."

    def handle(self, *args, **options):
        for model in get_models():
            opts = model._meta
            ctype, created = ContentType.objects.get_or_create(
                app_label=opts.app_label,
                model=opts.object_name.lower(),
                defaults={'name': smart_unicode(opts.verbose_name_raw)})

            for codename, name in _get_all_permissions(opts, ctype):
                p, created = Permission.objects.get_or_create(
                    codename=codename,
                    content_type=ctype,
                    defaults={'name': name})
                if created:
                    sys.stdout.write('Adding permission {}\n'.format(p))

            for permission in settings.PERMISSIONS:
                codename = permission[0]
                app_label = permission[1]
                module_name = permission[2]
                name = permission[3]

                content_type = ContentType.objects.get(app_label=app_label, model=module_name)
                p, created = Permission.objects.update_or_create(
                    codename=codename,
                    content_type=content_type,
                    defaults={
                        'name': name
                    }
                )
                if created and p:
                    sys.stdout.write('Adding permission %s\n' % p)

