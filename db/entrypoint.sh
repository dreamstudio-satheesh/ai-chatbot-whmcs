#!/bin/bash
set -e

echo "Updating PostgreSQL configurations..."

# Ensure PostgreSQL data directory exists
mkdir -p /var/lib/postgresql/data
chown -R postgres:postgres /var/lib/postgresql/data
chmod -R 700 /var/lib/postgresql/data

# Check if database is already initialized
if [ ! -f "/var/lib/postgresql/data/PG_VERSION" ]; then
    echo "Initializing new database..."
    gosu postgres initdb -D /var/lib/postgresql/data

    # Start PostgreSQL temporarily to set up the database
    echo "Starting PostgreSQL for initial setup..."
    gosu postgres pg_ctl -D /var/lib/postgresql/data -l /var/lib/postgresql/data/logfile start

    sleep 5  # Wait for PostgreSQL to start

    # Run init.sql only on first-time setup
    echo "Running initialization script..."
    gosu postgres psql -f /docker-entrypoint-initdb.d/init.sql

    # Stop PostgreSQL after setup
    echo "Stopping PostgreSQL after initialization..."
    gosu postgres pg_ctl -D /var/lib/postgresql/data stop

    # Mark database as initialized
    touch /var/lib/postgresql/data/db_initialized
else
    echo "Existing database detected. Skipping initialization..."
fi

# Copy configuration files
cp /etc/postgresql/pg_hba.conf /var/lib/postgresql/data/pg_hba.conf
cp /etc/postgresql/postgresql.conf /var/lib/postgresql/data/postgresql.conf
chown postgres:postgres /var/lib/postgresql/data/pg_hba.conf /var/lib/postgresql/data/postgresql.conf
chmod 600 /var/lib/postgresql/data/pg_hba.conf /var/lib/postgresql/data/postgresql.conf

# Start PostgreSQL in the foreground
echo "Starting PostgreSQL..."
exec gosu postgres postgres -D /var/lib/postgresql/data
