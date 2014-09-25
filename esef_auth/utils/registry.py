__author__ = 'ahmetdal'

import os
import sys


class Registry(object):
    """
    Abstract module loader/registry
    """
    name = "Registry"  # Registry name
    subdir = "directory"  # Restrict to directory
    classname = "Class"  # Auto-register class
    apps = None  # Restrict to a list of application
    exclude = []  # List of excluded modules
    exclude_daemons = []  # List of excluded daemons

    def __init__(self):
        self.classes = {}
        # Detect daemon name
        _, self.daemon_name = os.path.split(sys.argv[0])
        if self.daemon_name.endswith(".py"):
            self.daemon_name = self.daemon_name[:-3]
        if self.daemon_name == "manage":
            if len(sys.argv) > 1:
                self.daemon_name = sys.argv[1]
                #
        self.is_registered = self.daemon_name in self.exclude_daemons


    def register(self, name, module):
        """
        Should be called within metaclass' __new__ method
        """
        if name is None:
            return
        self.classes[name] = module

    def __getitem__(self, name):
        return self.classes[name]

    def __contains__(self, item):
        return item in self.classes

    def __iter__(self):
        for k, v in self.classes.iteritems():
            yield k, v

    @property
    def choices(self):
        """
        For model field's choices=
        """
        return [(x, x) for x in sorted(self.classes.keys())]