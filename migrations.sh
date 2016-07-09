#!/bin/bash
if [ "$1" = "-r" ]; then
    find . -name \migrations -type d -exec rm -r {} +
else 
    python manage.py makemigrations authentication bidding categories chat contact_us posts review spartans report error_pages
    python manage.py migrate
fi

