#!/bin/sh

# Wait for database connection
echo "Waiting for database connection..."
sleep 10

chown -R www-data:www-data /var/www/html/storage /var/www/html/bootstrap/cache
chmod -R 775 /var/www/html/storage /var/www/html/bootstrap/cache

# Setup Laravel
php artisan config:clear
php artisan cache:clear
php artisan view:clear
php artisan migrate:fresh
php artisan db:seed --force

# Start PHP-FPM
exec php-fpm