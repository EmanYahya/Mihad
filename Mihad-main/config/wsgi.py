import os

from django.core.wsgi import get_wsgi_application

# Set the DJANGO_SETTINGS_MODULE environment variable to your settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Activate the virtual environment (assuming it's located at /path/to/virtualenv)
#activate_this = 'myenv/bin/activate_this.py'
# with open(activate_this) as file_:
#    exec(file_.read(), dict(__file__=activate_this))

# Create the WSGI application
application = get_wsgi_application()
