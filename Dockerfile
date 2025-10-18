# Use PHP with Apache
FROM php:8.2-apache

# Copy application code
COPY app/ /var/www/html/

# Install mysqli extension for MySQL
RUN docker-php-ext-install mysqli

# Give Apache permission to serve files
RUN chown -R www-data:www-data /var/www/html && chmod -R 755 /var/www/html

# Expose port 80
EXPOSE 80
