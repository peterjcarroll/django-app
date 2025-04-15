#!/bin/bash
# This script runs the app locally while still using Docker for the database.

# start the database container
docker compose up -d db

# set the environment variables from .env file
export $(grep -v '^#' .env | xargs)

# override the database host to localhost
export POSTGRES_HOST=localhost

# run the database migrations
uv run manage.py migrate

# run the app
uv run manage.py runserver 0.0.0.0:8000