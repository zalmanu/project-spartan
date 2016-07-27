# Copyright 2015-2016 Emanuel Danci, Emanuel Covaci, Fineas Silaghi, Sebastian Males, Vlad Temian
#
# This file is part of Project Spartan.
#
# Project Spartan is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Project Spartan is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Project Spartan.  If not, see <http://www.gnu.org/licenses/>.
import os
from base import *



# SECRET_KEY
SECRET_KEY = 'er&cazxnks3w4jh_6(w5jq10^b05&evags5g%#@r5esleqt%t#'

# RECAPTCHA
RECAPTCHA_PUBLIC_KEY = '6LdWFh8TAAAAADQvDLA5vzxARRYvSmb0Hbioppik'
RECAPTCHA_PRIVATE_KEY = '6LdWFh8TAAAAAM_jX3R5CTLKP5slzYBmaybBjiP8'


#email settings
EMAIL_USE_TLS = True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='contactprojectspartan@gmail.com'#insert email
EMAIL_HOST_PASSWORD='spartan123456789'#insert password
EMAIL_PORT=587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DB_ENV_DB', 'postgres'),
        'USER': os.environ.get('DB_ENV_POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_ENV_POSTGRES_PASSWORD', ''),
        'HOST': os.environ.get('DB_PORT_5432_TCP_ADDR', ''),
        'PORT': os.environ.get('DB_PORT_5432_TCP_PORT', ''),
    }
}

# Celery settings
BROKER_URL = os.environ.get('SPARTAN_BROKER_URL', 'redis://192.168.99.100:6379/0')
CELERY_BROKER_URL = os.environ.get('SPARTAN_CELERY_BROKER_URL', 'redis://192.168.99.100:6379/0')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
