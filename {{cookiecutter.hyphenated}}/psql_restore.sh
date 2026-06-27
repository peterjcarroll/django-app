#!/bin/bash
set -e
APP_DIR=$(dirname "$(realpath "$0")")
cd "$APP_DIR"

# Load environment variables from .env file
if [ -f .env ]; then
    set -a
    source .env
    set +a
fi

# Override host for local access
POSTGRES_HOST=localhost

BACKUP_DIR="$APP_DIR/db_backups"

if [ ! -d "$BACKUP_DIR" ]; then
    echo "Error: Backup directory $BACKUP_DIR does not exist"
    exit 1
fi

if [ -z "$1" ]; then
    BACKUP_FILE=$(ls -1t "$BACKUP_DIR"/{{cookiecutter.hyphenated}}-*.sql.gz 2>/dev/null | head -n 1)
    if [ -z "$BACKUP_FILE" ]; then
        echo "Error: No backup files found in $BACKUP_DIR"
        exit 1
    fi
    echo "Using most recent backup: $BACKUP_FILE"
else
    BACKUP_FILE="$1"
    if [ ! -f "$BACKUP_FILE" ]; then
        echo "Error: Specified backup file $BACKUP_FILE does not exist"
        exit 1
    fi
    echo "Using specified backup: $BACKUP_FILE"
fi

echo "WARNING: This will drop and recreate the database $POSTGRES_DB"
echo "Press Ctrl+C to cancel, or any other key to continue..."
read -n 1 -s

echo "Restoring database from $BACKUP_FILE..."
gunzip -c "$BACKUP_FILE" | docker compose exec -T -e PGPASSWORD="$POSTGRES_PASSWORD" db psql -h localhost -U "$POSTGRES_USER" "$POSTGRES_DB"
echo "Database restore completed successfully"
