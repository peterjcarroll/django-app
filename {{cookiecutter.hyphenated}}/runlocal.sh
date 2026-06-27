#!/bin/bash
# This script runs the app locally while still using Docker for the database.

# install pre-commit hooks if not already installed
if [ ! -f ".git/hooks/pre-commit" ]; then
    uv run pre-commit install
fi

# start the database container
docker compose up -d db

# set the environment variables from .env file
set -a
source .env
set +a

# override the database host to localhost
export POSTGRES_HOST=localhost

# run the database migrations
uv run manage.py migrate

# run the app
uv run manage.py runserver 0.0.0.0:8000
