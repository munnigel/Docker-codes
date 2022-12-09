FROM php:7.4-fpm-alpine

# standard folder for laravel web servers to serve your website from
WORKDIR /var/www/html

# docker-php-ext-install is a tool to install PHP extensions, such as pdo_mysql and pdo
RUN docker-php-ext-install pdo pdo_mysql