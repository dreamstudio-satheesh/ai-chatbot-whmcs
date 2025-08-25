# ---------- Stage 1: Composer dependencies ----------
FROM composer:2 AS vendor
WORKDIR /app

# Leverage build cache: install deps based on composer files first
COPY composer.json composer.lock ./
RUN composer install \
    --no-dev \
    --prefer-dist \
    --no-progress \
    --no-interaction

# Now copy the rest of the app and optimize autoload
COPY . .
RUN composer install \
    --no-dev \
    --prefer-dist \
    --no-progress \
    --no-interaction \
    --optimize-autoloader


# ---------- Stage 2: PHP-FPM + Nginx runtime ----------
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
    libjpeg-dev \
    libfreetype6-dev \
    git \
 && rm -rf /var/lib/apt/lists/*

# PHP extensions (adjust as needed)
RUN docker-php-ext-configure gd --with-freetype --with-jpeg \
 && docker-php-ext-install -j$(nproc) gd pdo pdo_mysql zip

# Nginx & PHP-FPM config
WORKDIR /var/www/html
ENV PHP_FPM_LISTEN=9000
EXPOSE 9000

# Copy application (including vendor from builder)
COPY --from=vendor /app /var/www/html

# Set Laravel permissions
RUN chown -R www-data:www-data /var/www/html \
 && mkdir -p storage bootstrap/cache \
 && chown -R www-data:www-data storage bootstrap/cache \
 && find storage -type d -exec chmod 775 {} \; \
 && find storage -type f -exec chmod 664 {} \; \
 && chmod -R 775 bootstrap/cache

# (Optional) ensure .env exists at build or mount at runtime
# COPY .env /var/www/html/.env

# Supervisor & entrypoint
COPY supervisord.conf /etc/supervisord.conf
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# Start Supervisor (runs php-fpm & nginx as configured in supervisord.conf)
CMD ["sh", "/usr/local/bin/docker-entrypoint.sh"]
