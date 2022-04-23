#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from util.custom_logging import critical

if __name__ == '__main__':
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ascii_generator.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        critical("Couldn't import Django. Are you sure it's installed and\navailable on your PYTHONPATH environment variable? Did you\nforget to activate a virtual environment?")

    execute_from_command_line(sys.argv)
