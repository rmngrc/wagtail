from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vnim$0(gecx&k#ztddq^&3&pmft*6)(1to5g#s-7h!r6n3t%8!'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*'] 

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dev-uk',
        'USER': 'dev-uk',
        'PASSWORD': 'dev-uk',
        'HOST': 'db-uk',
        'PORT': 3306,
    }
}

try:
    from .local import *
except ImportError:
    pass
