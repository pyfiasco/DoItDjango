"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xy7wozejy@vtr#1pucv*$n5=j2*vs-^jnlzqkn)au6l+xznd38'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # 배포를 위해 False 설정

ALLOWED_HOSTS = ['127.0.0.1', 'neo21pow.pythonanywhere.com']   # host등록



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Local App
    'pages.apps.PagesConfig',
    'accounts.apps.AccountsConfig',    
    # 3rd Party
    'crispy_forms', 
    'crispy_bootstrap5',  # pip install crispy-bootstrap5  필요


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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path(BASE_DIR).joinpath('templates'),
                 ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'   # 'en-us'

TIME_ZONE = 'Asia/Seoul'  # 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = Path(BASE_DIR).joinpath('staticfiles')
STATICFILES_DIRS = [Path(BASE_DIR).joinpath('static')]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login redirect url 설정
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'


# accounts 설정 - 'auth.User' (기본사용)
AUTH_USER_MODEL = 'accounts.CustomUser'  # 사용자 정의 user사용



# pip install template 사용
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# 비밀번호 변경시 이메일 전송  -> console 확인
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# sendgrid를 통한 메일 전송위한 설정
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # sendgrid이용
DEFAULT_FROM_EMAIL = 'neo21pow@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
