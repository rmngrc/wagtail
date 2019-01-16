#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    print("LOCALE: " + os.environ['ZAVA_COUNTRY'])
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locales.%s.web.settings.dev" % os.environ['ZAVA_COUNTRY'])

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
