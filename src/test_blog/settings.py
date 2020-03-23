import os
import json

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


if os.environ.get('CONFIG_PATH') is None:
    CONFIG_PATH = os.path.dirname(BASE_DIR) + '/config.json'
else:
    CONFIG_PATH = os.environ['CONFIG_PATH']

with open(CONFIG_PATH) as f:
    CONFIG = json.load(f)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = CONFIG['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = CONFIG['DEBUG']

ALLOWED_HOSTS = CONFIG['ALLOWED_HOSTS']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core.apps.CoreConfig',
    'authentication.apps.AuthenticationConfig',
    'blog.apps.BlogConfig',
    'email_notifier.apps.EmailNotifierConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'test_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'test_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': CONFIG['DB_NAME'],
        'USER': CONFIG['DB_USER'],
        'PASSWORD': CONFIG['DB_PASSWORD'],
        'HOST': CONFIG['DB_HOST'],
        'PORT': CONFIG['DB_PORT'],
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = CONFIG['LANGUAGE_CODE']

TIME_ZONE = CONFIG['TIME_ZONE']

USE_I18N = CONFIG['USE_I18N']

USE_L10N = CONFIG['USE_L10N']

USE_TZ = CONFIG['USE_TZ']


# Login redirect

LOGIN_URL = 'login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'


# Override base user model

AUTH_USER_MODEL = 'authentication.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = CONFIG['STATIC_URL']


# Email sending

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = CONFIG['EMAIL_HOST']
EMAIL_HOST_USER = CONFIG['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = CONFIG['EMAIL_HOST_PASSWORD']
EMAIL_PORT = CONFIG['EMAIL_PORT']
EMAIL_USE_TLS = CONFIG['EMAIL_USE_TLS']
EMAIL_USE_SSL = CONFIG['EMAIL_USE_SSL']
