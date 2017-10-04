"""
Django settings for centurion project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url


DEPLOY = os.getenv('DEPLOY') != 'HEROKU'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

DEBUG = os.getenv('DJANGO_DEBUG') != 'FALSE'
# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    SECRET_KEY = '$dn+%59yjby20dr8e#(&cl4=38i_$-@hp8bm)x=-ln9i^-is89'
    ALLOWED_HOSTS = ['*']
else:
    SECRET_KEY = os.getenv('SECRET_KEY')
    ALLOWED_HOSTS = ['centurionmsc.pythonanywhere.com', 'centurionmsc.com', '.herokuapp.com']

# SECURITY WARNING: don't run with debug turned on in production!
   

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'content', 
    'blog',
    'tinymce',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

ROOT_URLCONF = 'centurion.urls'

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

WSGI_APPLICATION = 'centurion.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


if DEPLOY:
    ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'centurion',
            'USER': 'name',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES['default'].update(db_from_env)




TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,xhtmlxtras,spellchecker,paste,searchreplace, save, advhr, advimage, advlink, emotions, iespell, insertdatetime, preview",
    'theme_advanced_buttons1': "bold,italic,underline,strikethrough,sub,sup,separator,justifyleft,justifycenter,justifyright,justifyfull,separator,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2': "bullist,numlist,outdent,indent,ltr,rtl,separator,link,unlink,anchor,image,separator,table,insertdate,inserttime,advhr,emotions,media,charmap,separator,undo,redo, spellchecker",
    'theme': 'advanced',
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
    'elementpath': False,
    'height': 300,
    'width': 1000,
    'resize': 'both',

}
TINYMCE_SPELLCHECKER = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# Extra places for collectstatic to find static files.

