"""
WSGI config for {{cookiecutter.underscored}} project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.underscored}}.settings")

from {{cookiecutter.underscored}}.proctitle import apply_title, title_for_wsgi

apply_title(title_for_wsgi())

application = get_wsgi_application()
