#!/bin/bash
# This script runs the app locally while still using Docker for the database.

# start the database container
docker compose up -d db

# set the environment variables from .env file
export $(grep -v '^#' .env | xargs)

# override the database host to localhost
export POSTGRES_HOST=localhost

# pass the arguments to the manage.py script
uv run manage.py "$@"