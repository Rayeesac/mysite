import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '=z=_^h^f*6v+ikgiv3(_5rr(i)4q&7^q=t-fnc3d*su7zc7zhv'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','localhost','10.0.0.89']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'afl_user',
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

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {   
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
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

TEMPLATE_DEBUG = True

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database

# postgresql

#Database for eps89
######################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Mysite',
        'USER': 'postgres',
        'PASSWORD': 'epsadmin',
        'HOST': 'localhost',
        'PORT':'5432',
    }
}

######################


#rac-thinkpad
######################

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'Mysite',
#         'USER': 'root',
#         'PASSWORD': 'password',
#         'HOST': 'localhost',
#         'PORT':'5432',
#     }
# }

######################

# mysql
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'Mysite',
#         'USER': 'root',
#         'PASSWORD': 'epsadmin',
#         'HOST': 'localhost',
#         'PORT':'3306',
#     }
# }


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


LOGOUT_REDIRECT_URL = 'home'

LOGIN_REDIRECT_URL = 'home'

LOGIN_URL = 'user/login'

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

######## EMAIL #######

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True  
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587  
EMAIL_HOST_USER = 'developer4mysite@gmail.com'  
EMAIL_HOST_PASSWORD = 'developer@2020'  

#######  GOOGLE_RECAPTCHA_SECRET_KEY  #########

GOOGLE_RECAPTCHA_SECRET_KEY = "6LdeitgUAAAAAAQwA0xMH908W53JQxGfoOJdVxyZ"

############  ##############

MEDIA_URL = '/media/'
MEDIA_ROOT =  os.path.join(BASE_DIR, 'media')
