#!/bin/bash
set -e

# Run migrations if DB_HOST is set (skip in tests)
if [ -n "$DB_HOST" ]; then
    alembic upgrade head
fi

# Execute the main command (CMD from Dockerfile)
exec "$@"