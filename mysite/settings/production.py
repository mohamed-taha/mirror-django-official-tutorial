from .base import *
from .base import env

DEBUG = False

ALLOWED_HOSTS = []  # TODO: Update when deploying to prod

SECRET_KEY = env("DJANGO_SECRET_KEY")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env.str('DATABASE_NAME'),
        'USER': env.str('DATABASE_USER'),
        'PASSWORD': env.str('DATABASE_PASSWORD'),
        'HOST': env.str('DATABASE_HOST'),
    }
}