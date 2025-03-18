#!/bin/bash
set -e

echo "🚀 Running PostgreSQL user initialization script..."

# Wait for PostgreSQL to start
sleep 5

# Set the user password
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    ALTER USER postgres WITH PASSWORD '${POSTGRES_PASSWORD}';
EOSQL

echo "✅ PostgreSQL user setup completed!"
