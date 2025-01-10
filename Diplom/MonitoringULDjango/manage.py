#!/usr/bin/env python
"""
Command-line utility for administrative tasks.

# For more information about this file, visit
# https://docs.djangoproject.com/en/2.1/ref/django-admin/
"""

import os
import sys
from threading import Thread, Lock
from app.tgbot import *

def start_tg_bot():
    bot.polling(none_stop=True, interval=0)

def start_web_app():
    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'MonitoringULDjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    th2 = Thread(target=start_web_app)
    th2.start()
    start_tg_bot()

