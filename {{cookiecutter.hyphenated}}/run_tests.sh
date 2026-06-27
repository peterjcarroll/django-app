#!/bin/bash
# Run Django tests locally against the Docker database.

# start the database container if not already running
docker compose up -d db

# set the environment variables from .env file
set -a
source .env
set +a

# override the database host to localhost
export POSTGRES_HOST=localhost

uv run manage.py test "$@"
