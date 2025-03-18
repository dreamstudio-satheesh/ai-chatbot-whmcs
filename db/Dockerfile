FROM postgres:14.1-alpine

WORKDIR /var/lib/postgresql

# Install gosu to correctly switch users
RUN apt-get update && apt-get install -y gosu

# Copy scripts and configurations
COPY entrypoint.sh /entrypoint.sh
COPY pg_hba.conf /etc/postgresql/pg_hba.conf
COPY postgresql.conf /etc/postgresql/postgresql.conf

# Ensure scripts are executable
RUN chmod +x /entrypoint.sh

# Set the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]
