FROM php:8.3-fpm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    unzip \
    curl \
    libpq-dev \
    nginx \
    supervisor \
    redis \
    libzip-dev \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    sqlite3 \
    && docker-php-ext-install pdo pdo_pgsql bcmath \
    && pecl install redis \
    && docker-php-ext-enable redis

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/*


# Set working directory
WORKDIR /var/www/html

# Copy application files
COPY . .

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Install PHP dependencies
RUN composer install --no-dev --optimize-autoloader

# Set permissions
# RUN chown -R www-data:www-data /var/www/html/storage /var/www/html/bootstrap/cache
# RUN chmod -R 775 /var/www/html/storage /var/www/html/bootstrap/cache

# Copy Supervisor configuration for managing queue workers & WebSockets
COPY supervisord.conf /etc/supervisord.conf

# Entrypoint script for migrations
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Expose ports
EXPOSE 9000

# Start Supervisor
CMD ["sh", "/usr/local/bin/docker-entrypoint.sh"]