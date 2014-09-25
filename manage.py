#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "esef_sso_server.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "esef_auth.settings")
>>>>>>> 8b685542c998b8c22f53efb0635b1d60e1e7a4d6

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
