FROM composer:latest

WORkDIR /var/www/html

ENTRYPOINT [ "composer", "--ignore-platform-reqs" ]