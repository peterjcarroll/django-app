# {{ cookiecutter.app_name }}

{{ cookiecutter.description }}

This [Django](https://www.djangoproject.com/) application requires [uv](https://github.com/astral-sh/uv) and [Docker Compose](https://docs.docker.com/compose/) to be installed.

## Setup
Copy `env.example` to `.env` and set strong values for `POSTGRES_PASSWORD` and `DJANGO_SECRET_KEY` in the `.env` file. This file is in `.gitignore` to prevent passwords from being included in the git repo.

## Running
This project can be run for development using either `uv` or `docker compose`. In both cases, the database will run under `docker compose`.

### Running locally using uv
1. Make sure `uv` is installed.
2. Run `uv sync` to pull down all the dependencies if you haven't done so already.
3. Run `./runlocal.sh` to start the application. 

To run django management commands like `createsuperuser`, run:
`./localmanage.sh createsuperuser`

### Running using docker compose
1. Make sure `docker compose` is installed.
2. Run `docker compose up -d --build && docker compose logs -f` to start the application.

To run django management commands like `createsuperuser`, run:
`docker compose exec web uv run manage.py createsuperuser`
