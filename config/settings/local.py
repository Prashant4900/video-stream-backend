print('********************************************************')
print('*******************  local.py  *************************')
print('********************************************************')

from .base import ALLOWED_HOSTS, BASE_DIR

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+c1x)ge&o4^#b_y$m0tb_@=#wcp5i&2xk+x0(9x2n!g4+zt5eg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS += ['127.0.0.1']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_HOST = ""

FILER_DEBUG = True
FILER_ENABLE_LOGGING = True
