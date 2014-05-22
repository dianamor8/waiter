"""
Django settings for waiter project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATE_DIRS = (os.path.join(BASE_DIR,'waiter/templates'),)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'one3&!(!tgz&7d_@g3_aam!1a^ke_+5u)dc2ukrqk4t09=3hvn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'waiter.apps.usuarios',
    'waiter.apps.producto',
    'waiter.apps.home',
    'waiter.apps.pedido',
    'waiter.apps.webservices.wsProductos',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'waiter.urls'

WSGI_APPLICATION = 'waiter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'waiter',#os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': 'waiter',
        'PASSWORD':'waiter',
        'HOST':'localhost',
        'PORT':'5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#AQUI LA CONFIGURACION DEL CORREO
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'mp.dianalexa@gmail.com'
EMAIL_HOST_PASSWORD = 'morochitodiana1105'
EMAIL_USE_TLS = True
#


#SERVIDOR DE MEDIOS 
MEDIA_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'waiter/media/'))
MEDIA_URL = '/media/'
#SERVIDOR DE MEDIOS


#PARA REDIRECCIONAR EL LOGIN
LOGIN_URL = '/usuarios/login/'
LOGIN_REDIRECT_URL = '/'


