#!/bin/bash
if [ "$1" = "-r" ]; then
    find . -name \migrations -type d -exec rm -r {} +
else 
    python spartan/manage.py makemigrations authentication bidding categories chat contact_us posts review spartans report notifications
    python spartan/manage.py migrate
fi

