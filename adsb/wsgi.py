"""
WSGI config for adsb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'adsb.settings')

# application = get_wsgi_application()

import os, sys

sys.path.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR']))

os.environ['DJANGO_SETTINGS_MODULE'] = 'adsb.settings'

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'

os.environ['PYTHON_EGG_CACHE'] = os.path.join(virtenv, 'lib/python3.6/site-packages')

virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
    execfile(virtualenv, dict(file=virtualenv))
except IOError:
    pass

# Postgres environment variables
os.environ['POSTGRES_USER'] = 'futurecapability'
os.environ['POSTGRES_PASS'] = 'BAECommTech1'
os.environ['POSTGRES_HOST'] = '172.21.157.88'
os.environ['POSTGRES_PORT'] = '5432'
os.environ['POSTGRES_DATABASE'] = 'adsb_data'

#
# IMPORTANT: Put any additional includes below this line.  If placed above this
# line, it's possible required libraries won't be in your searchable path
#

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()