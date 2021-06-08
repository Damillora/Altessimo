from altessimo.settings import *
import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('ALTESSIMO_DB_NAME'),
        'USER': os.getenv('ALTESSIMO_DB_USER'),
        'PASSWORD': os.getenv('ALTESSIMO_DB_PASS'),
        'HOST': os.getenv('ALTESSIMO_DB_HOST'),
    }
}

ALLOWED_HOSTS = [ os.getenv('ALTESSIMO_WEB_URL') ]
