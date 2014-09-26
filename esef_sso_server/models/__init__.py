from esef_auth.models import filtered_class_registry
from simple_sso.sso_server.models import Consumer

__author__ = 'ahmetdal'

filtered_class_registry.register(Consumer._meta.module_name, Consumer)