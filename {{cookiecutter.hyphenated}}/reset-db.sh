#!/bin/bash
# Reset the database by removing its volume and restoring from the most recent backup.
# WARNING: This deletes all data in the local database.

set -e
APP_DIR=$(dirname "$(realpath "$0")")
cd "$APP_DIR"

if [ ! -d "db_backups" ]; then
    echo "Error: db_backups directory does not exist"
    exit 1
fi

if [ -z "$(ls -1 db_backups/{{cookiecutter.hyphenated}}-*.sql.gz 2>/dev/null)" ]; then
    echo "Error: No backup files found in db_backups directory"
    exit 1
fi

docker compose down --volumes
docker compose up -d db
./psql_restore.sh
./localmanage.sh migrate
