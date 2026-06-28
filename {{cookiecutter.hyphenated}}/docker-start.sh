#!/usr/bin/env bash
set -e

if [ "$1" = 'granian' ] || [ -z "$1" ]; then
    uv run granian --interface asgi --host 0.0.0.0 --port 8000 {{cookiecutter.underscored}}.asgi:application
elif [ "$1" = 'collectstatic' ]; then
    uv run manage.py collectstatic --noinput
elif [ "$1" = 'migrate' ]; then
    uv run manage.py migrate
elif [ "$1" = 'runserver' ]; then
    uv run manage.py runserver 0.0.0.0:8000
elif [ "$1" = 'manage' ]; then
    shift
    uv run manage.py "$@"
else
    exec "$@"
fi
