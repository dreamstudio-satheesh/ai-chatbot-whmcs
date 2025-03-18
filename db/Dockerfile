FROM postgres:15

# Install pgvector extension
RUN apt-get update && apt-get install -y postgresql-contrib

# Copy initialization script for first-time database setup
COPY init.sql /docker-entrypoint-initdb.d/init.sql
