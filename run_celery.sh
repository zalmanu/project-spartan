#!/bin/sh

cd spartan
# run Celery worker for our project myproject with Celery configuration stored in Celeryconf
su -m myuser -c "celery worker -A config.celeryconf -Q default -n default@%h"
