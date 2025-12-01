from pathlib import Path
import os # Nécessaire pour lire RENDER_EXTERNAL_HOSTNAME

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&zl*i&kolh=7v!u@nh9acn*bjo3_nly$)!xaym^3&8169ea&7!'

# --- CORRECTION 1 : DEBUG DOIT ÊTRE FALSE EN PRODUCTION ---
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# --- CORRECTION 2 : AUTORISER L'HÔTE RENDER ---
# Lit le nom d'hôte externe que Render injecte dans l'environnement
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

if RENDER_EXTERNAL_HOSTNAME:
    # Autorise l'URL Render et les adresses locales
    ALLOWED_HOSTS = [RENDER_EXTERNAL_HOSTNAME, '127.0.0.1', 'localhost']
else:
    # Fallback pour le développement local
    ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',         
    'django_filters',         
    'courseservice',
]

# --- CORRECTION 3 : AJOUT DU MIDDLEWARE WHITENOISE ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Doit être placé juste après SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mini_projet_idl.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mini_projet_idl.wsgi.application'


# Database
# Les identifiants sont ceux que vous avez fournis (en dur)
DATABASES = {
    'default': { 
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'student_es69', 
        'USER': 'student_es69_user', 
        'PASSWORD': 'omBsaDurmHQ70VHQXBiymmurFOPJPhak', 
        'HOST': 'dpg-d4inutnpm1nc73crbee0-a', 
        'PORT': '5432',
    }
}


# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# --- CONFIGURATION DES FICHIERS STATIQUES ---
STATIC_URL = 'static/'
# Répertoire où Django va collecter les fichiers statiques (OBLIGATOIRE pour WhiteNoise)
STATIC_ROOT = BASE_DIR / 'staticfiles' 

# Utiliser le backend WhiteNoise pour servir les fichiers statiques en prod
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'