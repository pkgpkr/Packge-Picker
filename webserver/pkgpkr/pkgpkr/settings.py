"""
Django settings for pkgpkr project.

Generated by 'django-admin startproject' using Django 2.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import requests

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2@)h)0oz7su2wdinjl9ni5w%wa7+4l9s1c)!3%a1#ya6quow-3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Add the container IP address as an allowed host if it exists
if os.environ.get('ECS_CONTAINER_METADATA_URI'):
  METADATA_URI = os.environ['ECS_CONTAINER_METADATA_URI']
  container_metadata = requests.get(METADATA_URI).json()
  ALLOWED_HOSTS.append(container_metadata['Networks'][0]['IPv4Addresses'][0])

# Application definition

INSTALLED_APPS = [
    'webservice',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

ROOT_URLCONF = 'pkgpkr.urls'

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

WSGI_APPLICATION = 'pkgpkr.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# Env keys
GITHUB_CLIENT_ID = os.environ.get('CLIENT_ID')
GITHUB_CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

# Github auth config
GITHUB_SCOPE = 'repo'
GITHUB_ALLOW_SIGN_UP = 'false'

# Endpoints
GITHUB_BASE_URL = 'https://github.com'
APP_GITHUB_CALLBACK_URI = 'http://localhost:8000/callback'
GITHUB_OATH_AUTH_PATH = f'{GITHUB_BASE_URL}/login/oauth/authorize?client_id={GITHUB_CLIENT_ID}&' \
    f'allow_signup={GITHUB_ALLOW_SIGN_UP}&redirect_uri={APP_GITHUB_CALLBACK_URI}&scope={GITHUB_SCOPE}'
GITHUB_OATH_ACCESS_TOKEN_PATH = f'{GITHUB_BASE_URL}/login/oauth/access_token'
GITHUB_OATH_REVIEW_AUTHORIZATIONS_PATH = f'{GITHUB_BASE_URL}/settings/connections/applications/{GITHUB_CLIENT_ID}'

GITHUB_BASE_API_URL = 'https://api.github.com'
GITHUB_USER_INFO_URL = f'{GITHUB_BASE_API_URL}/user'
GITHUB_GRAPHQL_URL = 'https://api.github.com/graphql'

NPM_DEPENDENCY_BASE_URL = 'https://npmjs.com/package'
