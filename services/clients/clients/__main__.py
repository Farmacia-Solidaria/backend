import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clients.settings')
from django.core.management import execute_from_command_line  # noqa: E402

# Override default port for `runserver` command
from django.core.management.commands.runserver import Command as runserver
runserver.default_port = os.getenv("SERVICE_PORT")
runserver.default_addr = os.getenv("SERVICE_ADDR")

execute_from_command_line(sys.argv)
