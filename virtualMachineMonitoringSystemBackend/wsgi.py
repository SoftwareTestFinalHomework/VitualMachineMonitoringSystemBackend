"""
WSGI config for virtualMachineMonitoringSystemBackend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from virtualMachineMonitoringSystemBackend.config.virtual_machine_config import virtual_machine_list
from virtualMachineMonitoringSystemBackend.influx.write_data import WriteMachineData

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'virtualMachineMonitoringSystemBackend.settings')

for item in virtual_machine_list:
    WriteMachineData(item).start()
    print(item)

application = get_wsgi_application()
