from .base import *
from .base import env

DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = env("DJANGO_SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DATABASE_NAME', default='mysite'),
        'USER': env.str('DATABASE_USER', default='postgres'),
        'PASSWORD': env.str('DATABASE_PASSWORD', default='postgres'),
        'HOST': env.str('DATABASE_HOST', default='localhost'),
    }
}