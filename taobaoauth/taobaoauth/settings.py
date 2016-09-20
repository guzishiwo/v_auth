"""
Django settings for taobaoauth project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
#coding=utf-8
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3!!#hd()_7zidyx(4v8l$8tg7mt7rrp92ii$tyqso3=n4zwx1#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = '*'

# Application definitio

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jd',
    'taobao',
    'identity',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'taobaoauth.urls'

WSGI_APPLICATION = 'taobaoauth.wsgi.application'



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
             'format': '%(levelname)s %(asctime)s %(message)s',
        },
    },
    'filters': {

    },
    'handlers': {
        'viewstofile':
        {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter':'standard',
            'filename': '/var/we_build_auth/taobao_auth.log',
        },
        'console':
        {
        'level': 'DEBUG',
        'class': 'logging.StreamHandler',
        'formatter': 'standard'
        },
        'apitofile':
        {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': '/var/we_build_auth/taobao_api.log',
        }
    },
    'loggers': {
        'taobao.views': {
            'handlers': ['viewstofile', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'taobao.api': {
            'handlers': ['apitofile', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
import logging
import logging.config
logging.config.dictConfig(LOGGING)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['MYSQL_INSTANCE_NAME'],
        'USER': os.environ['MYSQL_USERNAME'],
        'PASSWORD': os.environ['MYSQL_PASSWORD'],
        'HOST': os.environ['MYSQL_PORT_3306_TCP_ADDR'],
        'PORT': os.environ['MYSQL_PORT_3306_TCP_PORT']
    }
}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
# }

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
