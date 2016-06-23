
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
    'widget_tweaks',

    # Usual apps
    'authentication',
    'homepages',
    'posts',
    'bidding',
    'contactUS',
    'chat',
    'categories',
    'spartans',
    'profiles',
    'review',
    'faq',
    'report',
    'errorPages',
    'aboutUS',

)


MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'Spartan.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/templates/'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


WSGI_APPLICATION = 'Spartan.wsgi.application'


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.sqlite3',
         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "staticcollected")

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.'
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

DATE_FORMAT = 'd/m/Y'

TIME_FORMAT = 'H : i'

TIME_INPUT_FORMAT = 'H : i'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

LOGIN_URL = '/login/'

USE_I18N = True

USE_L10N = False

USE_TZ = True

NOCAPTCHA = True
RECAPTCHA_USE_SSL = False


# SECRET_KEY
SECRET_KEY = os.getenv('SPARTAN_SECRET_KEY', '')

# RECAPTCHA
RECAPTCHA_PUBLIC_KEY = os.getenv('SPARTAN_RECAP_PUBLIC', '')
RECAPTCHA_PRIVATE_KEY = os.getenv('SPARTAN_RECAP_PRIVATE', '')


# email settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = os.getenv('SPARTAN_HOST_USER', '')  # insert email
EMAIL_HOST_PASSWORD = os.getenv('SPARTAN_HOST_PASSWORD', '')  # insert password
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
