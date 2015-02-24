"""
Django settings for medirecord project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
#This code is to work with Heroku---------------------
import dj_database_url
import os

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# Static asset configuration
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

#Fin del codigo de Heroku

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0^%jzfs(w!2(d^+xi!!sqg$aw#ik@y)fmqcl-fh2-bnu&o9ya7'
#SECRET_KEY = os.environ.get('SECRET_KEY', DEFAULT_SECRET_KEY)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'medirecord.urls'

WSGI_APPLICATION = 'medirecord.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    #'default': {
    #    'ENGINE': 'django.db.backends.sqlite3',
    #    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd689bqgqcrpuu9',
        'USER': 'dfraoofrzztoil',
        'PASSWORD': 'uYgKe7OcHgYBIoW5b0EES5nqlC',
        'HOST': 'ec2-107-22-249-214.compute-1.amazonaws.com',
    }

    #'default': {
    #    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #    'NAME': 'medirecord'
    #    ),
    #}    
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Allow all host headers
ALLOWED_HOSTS = ['*']

DATABASES['default'] = dj_database_url.config()

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

#STATIC_URL = '/static/'
