# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
