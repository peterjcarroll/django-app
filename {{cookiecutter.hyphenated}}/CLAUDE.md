# Repository Agent Instructions

## Project Overview

This is a Django application: **{{ cookiecutter.app_name }}**

### Backend
- **Framework**: Django, project package in `{{cookiecutter.underscored}}/`
- **Apps**: `core` (main app), `uilib` (reusable UI components)
- **Database**: PostgreSQL (started via Docker Compose)
- **Package manager**: [`uv`](https://github.com/astral-sh/uv)

### Frontend
- **Styling**: [BeerCSS](https://www.beercss.com/) (Material Design 3)
- **Interactivity**: [htmx](https://htmx.org/) for partial page updates, [Alpine.js](https://alpinejs.dev/) for client-side state
- **Rendering**: Server-side Django templates with progressive enhancement
- **Assets**: Vendor JS/CSS self-hosted in `static/vendor/` — run `./scripts/update-vendor.sh` to update

## Development Workflow

### Running the Application
```bash
./runlocal.sh
```
Starts the Docker database, runs migrations, and launches the dev server at `http://localhost:8000`.

### Running Tests
```bash
./run_tests.sh
```
Starts the Docker database if needed and runs Django tests.

### Django Management Commands
```bash
./localmanage.sh <command>
```
Runs any Django management command against the local database.

### Docker
- `docker-start.sh` is the production entrypoint (uvicorn by default)
- `docker-compose.yml` is for **local development only**
- Production docker-compose is maintained separately

## Deployment

Two environments on the same server:
- **Test**: `/home/{{cookiecutter.github_username}}/{{cookiecutter.hyphenated}}-test` (deployed from `main` branch)
- **Production**: `/home/{{cookiecutter.github_username}}/{{cookiecutter.hyphenated}}` (deployed from `prod` branch)

GitHub Actions builds the Docker image, pushes to GHCR, and the self-hosted runner pulls and restarts the container.

## Frontend Guidelines

### Styling
- Use BeerCSS components and utility classes
- All pages extend `core/templates/core/base.html`
- Reusable UI fragments go in `uilib/templates/uilib/`

### Interactivity
- **htmx first**: use `hx-get`, `hx-post`, `hx-target`, `hx-swap` for dynamic updates
- **Alpine.js second**: use `x-data`, `x-show`, `x-bind` only when client-side state is needed
- Keep JavaScript minimal — prefer server-rendered HTML over JSON APIs

### Updating Vendor Assets
```bash
./scripts/update-vendor.sh
```
Downloads pinned versions of BeerCSS, htmx, and Alpine.js to `static/vendor/`. Edit version pins at the top of that script to upgrade.

## Code Style
- Linter/formatter: **ruff** (configured in `ruff.toml`)
- Pre-commit hooks installed automatically by `runlocal.sh`
- Run manually: `uv run ruff check . --fix && uv run ruff format .`

## File Structure
- `{{cookiecutter.underscored}}/` — Django project settings, urls, wsgi/asgi
- `core/` — main application logic
- `uilib/` — reusable UI template components
- `static/vendor/` — self-hosted frontend assets
- `scripts/` — developer utility scripts
- `db_backups/` — local database backup files (gitignored)
