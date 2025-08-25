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
    libjpeg-dev \
    libfreetype6-dev \
    sqlite3 \
    git \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install pdo pdo_mysql pdo_pgsql bcmath gd zip mbstring xml \
    && pecl install redis \
    && docker-php-ext-enable redis

# Cleanup
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Composer first
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Set working directory
WORKDIR /var/www/html

# Copy composer files first (better caching)
COPY composer.json composer.lock ./

# Install dependencies without scripts/autoloader first
RUN composer install --no-dev --no-scripts --no-autoloader

# Copy rest of application
COPY . .

# Now complete the composer install
RUN composer dump-autoload --optimize --no-dev

# Verify vendor directory was created
RUN echo "=== Final verification ===" \
    && ls -la /var/www/html/vendor/autoload.php \
    && echo "SUCCESS: autoload.php found!"

# Set permissions
RUN chown -R www-data:www-data /var/www/html \
    && mkdir -p /var/www/html/storage/logs \
    && mkdir -p /var/www/html/bootstrap/cache \
    && chown -R www-data:www-data /var/www/html/storage /var/www/html/bootstrap/cache \
    && chmod -R 775 /var/www/html/storage /var/www/html/bootstrap/cache

# Copy Supervisor configuration for managing queue workers & WebSockets
COPY supervisord.conf /etc/supervisord.conf

# Entrypoint script for migrations
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Expose ports
EXPOSE 9000

# Start Supervisor
CMD ["sh", "/usr/local/bin/docker-entrypoint.sh"]