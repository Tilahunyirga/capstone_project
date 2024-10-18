"""
WSGI config for E_Commerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'E_Commerce.settings')

application = get_wsgi_application()


import os
import sys

# Add your project directory to the Python path
path = '/home/yourusername/capstone_project'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'capstone_project.settings'

# Activate the virtual environment
activate_env = '/home/yourusername/.virtualenvs/capstone_env/bin/activate_this.py'
with open(activate_env) as f:
    exec(f.read(), dict(__file__=activate_env))

# Import Django's WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
