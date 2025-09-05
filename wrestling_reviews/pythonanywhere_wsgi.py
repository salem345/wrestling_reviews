# This file contains the WSGI configuration required to serve up your
# web application at http://<your-username>.pythonanywhere.com/
# It works by setting the variable 'application' to a WSGI handler of some
# description.

import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/wrestling_reviews'  # Replace 'yourusername' with your actual PythonAnywhere username
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'wrestling_reviews.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()