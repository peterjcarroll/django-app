"""
ASGI config for {{cookiecutter.underscored}} project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.underscored}}.settings")

from {{cookiecutter.underscored}}.proctitle import apply_title, title_for_asgi

apply_title(title_for_asgi())

application = get_asgi_application()
