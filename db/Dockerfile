# Use the official PostgreSQL image
FROM postgres:15

# Copy initialization files
COPY init.sql /docker-entrypoint-initdb.d/
COPY pg_hba.conf /var/lib/postgresql/data/
COPY init-user.sh /docker-entrypoint-initdb.d/

# Ensure the init-user.sh script is executable
RUN chmod +x /docker-entrypoint-initdb.d/init-user.sh

# Default PostgreSQL startup
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["postgres"]
