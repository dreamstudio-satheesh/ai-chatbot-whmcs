# --- Stage 1: Build Composer Dependencies ---
    FROM php:8.3-cli AS composer

    WORKDIR /app
    
    # Install only what's needed to build
    RUN apt-get update && apt-get install -y unzip curl git libzip-dev \
        && docker-php-ext-install zip
    
    # Install Composer
    RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
    
    # Copy only composer files first to cache dependencies
    COPY . .
    
    # Install PHP dependencies without dev
    RUN composer install --no-dev --optimize-autoloader
    
    # --- Stage 2: Final Laravel App Image ---
    FROM php:8.3-fpm
    
    # Install only runtime dependencies
    RUN apt-get update && apt-get install -y \
        libpq-dev \
        redis \
        libzip-dev \
        libpng-dev \
        libonig-dev \
        libxml2-dev \
        sqlite3 \
        && docker-php-ext-install pdo pdo_pgsql bcmath zip \
        && pecl install redis \
        && docker-php-ext-enable redis \
        && apt-get purge -y --auto-remove unzip curl git \
        && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
    
    WORKDIR /var/www/html
    
    # Copy only Laravel app files
    COPY . .
    
    # Copy dependencies from builder stage
    COPY --from=composer /app/vendor ./vendor
    
    # Set Laravel permissions
    RUN chown -R www-data:www-data storage bootstrap/cache \
        && chmod -R 775 storage bootstrap/cache
    
    # Copy entrypoint
    COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
    RUN chmod +x /usr/local/bin/docker-entrypoint.sh
    
    EXPOSE 9000
    CMD ["sh", "/usr/local/bin/docker-entrypoint.sh"]
    