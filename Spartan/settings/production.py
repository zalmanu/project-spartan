import os
import local
from base import *



SECRET_KEY =local.SECRET_KEY


RECAPTCHA_PUBLIC_KEY = local.RECAPTCHA_PUBLIC_KEY
RECAPTCHA_PRIVATE_KEY = local.RECAPTCHA_PRIVATE_KEY



#email settings
EMAIL_USE_TLS = True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER=local.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD=local.EMAIL_HOST_PASSWORD
EMAIL_PORT=587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'





