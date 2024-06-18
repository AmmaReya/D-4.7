"""
Django settings for NewsPaper project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vqrjgnk8waei6)0i+mt!yv*ct_ivp25c00knfv(ws*j(v6xr81'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'accounts',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'fpages',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    'django_apscheduler',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'allauth.account.middleware.AccountMiddleware'
]

ROOT_URLCONF = 'NewsPaper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'NewsPaper.wsgi.application'

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

LOGIN_REDIRECT_URL = "/news"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_URL = 'http://127.0.0.1:8000'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

EMAIL_BACKAND = 'django.core.mail.backends.console.EmailBackends'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
DEFAULT_FROM_EMAIL = ''

APSCHEDULER_DATETIME_FORMAT = 'N j, Y, f:s a'
APSCHEDULER_RUN_NOW_TIMEOUT = 25

ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'loggers': {
        'django': {
            'level': 'DEBUG',
            'handlers': ['console_INFO_handler', 'console_DEBUG_handler', 'console_WARNING_handler',
                         'console_ERROR_CRITICAL_handler', 'file_general_handler'],
            'propagate': True,
        },
        'django_request': {
            'level': 'ERROR',
            'handlers': ['file_errors_handler', 'mail_admins_handler'],
            'propagate': True,
        },
        'django_server': {
            'level': 'ERROR',
            'handlers': ['file_errors_handler', 'mail_admins_handler'],
            'propagate': True,
        },
        'django_template': {
            'level': 'ERROR',
            'handlers': ['file_errors_handler'],
            'propagate': True,
        },
        'django_db.backends': {
            'level': 'ERROR',
            'handlers': ['file_errors_handler'],
            'propagate': True,
        },
        'django_security': {
            'level': 'INFO',
            'handlers': ['file_security_handler'],
            'propagate': False,
        },
    },
    'handlers': {
        'console_INFO_handler': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_info_formatter',
        },
        'console_DEBUG_handler': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_debug_formatter',
        },
        'console_WARNING_handler': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_warning_formatter',
        },
        'console_ERROR_CRITICAL_handler': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'console_error_critical_formatter',
        },
        'file_general_handler': {
            'level': 'INFO',
            'filename': 'general.log',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'formatter': 'file_general_formatter',
        },
        'file_errors_handler': {
            'level': 'ERROR',
            'filename': 'error.log',
            'class': 'logging.FileHandler',
            'formatter': 'file_errors_formatter',
        },
        'file_security_handler': {
            'level': 'INFO',
            'filename': 'security.log',
            'class': 'logging.FileHandler',
            'formatter': 'file_security_formatter',
        },
        'mail_admins_handler': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'email_error_formatter',
        },
    },
    'formatters': {
        'console_info_formatter': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
            'datefmt': '%d.%m.%Y %H-%M-%S'
        },
        'file_general_formatter': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
            'datefmt': '%d.%m.%Y %H-%M-%S'
        },
        'console_debug_formatter': {
            'format': '%(asctime)s %(levelname)s %(message)s',
            'datefmt': '%d.%m.%Y %H-%M-%S'
        },
        'console_warning_formatter': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
            'datefmt': '%d.%m.%Y %H-%M-%S'
        },
        'file_errors_formatter': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s',
            'datefmt': '%d.%m.%Y %H-%M-%S'
        },
        'console_error_critical_formatter': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s %(exc_info)s',
            'datefmt': '%d.%m.%Y %H-%M-%S'
        },
        'file_security_formatter': {
            'format': '%(asctime)s %(levelname)s %(module)s %(message)s',
            'datefmt': '%d.%m.%Y %H-%M-%S'
        },
        'email_error_formatter': {
            'format': '%(asctime)s %(levelname)s %(message)s %(pathname)s',
            'datefmt': '%d.%m.%Y %H-%M-%S'
        },
    },
    'filters': {
        'require_debug_true': {'()': 'django.utils.log.RequireDebugTrue', },
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse', },
    },
}
