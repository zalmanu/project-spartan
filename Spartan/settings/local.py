import os
from base import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'er&cazxnks3w4jh_6(w5jq10^b05&evags5g%#@r5esleqt%t#'

RECAPTCHA_PUBLIC_KEY = '6LfOhB4TAAAAAIP6Nw60oYoCdr0OAfDNxkIZa9U7'
RECAPTCHA_PRIVATE_KEY = '6LfOhB4TAAAAADtMc7XrFyCi5AWP1c8a-AakPs_m'


#email settings
EMAIL_USE_TLS = True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='contactprojectspartan@gmail.com'#insert email
EMAIL_HOST_PASSWORD='spartan123456789'#insert password
EMAIL_PORT=587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'





