from pathlib import Path
import logging
import os

import coloredlogs
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "mysecretisnevertobefound"),
    LOGLEVEL=(str, "INFO"),
    REDIS_HOST=(str, "localhost"),
)

environ.Env.read_env(os.path.join(BASE_DIR, ".env"))
coloredlogs.install(level=env("LOGLEVEL"))
logger = logging.getLogger("CTF.web")

DEBUG = env("DEBUG") is True
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="127.0.0.1").split(",")
CSRF_TRUSTED_ORIGINS = [f"https://{host}" for host in ALLOWED_HOSTS]
logger.info(f"Allowed hosts {ALLOWED_HOSTS}")

REDIS_HOST = env("REDIS_HOST")

if DEBUG:
    logger.warning("The application is running in debug mode")

INTERNAL_IPS = [
    "127.0.0.1",
]

# Application definition
INSTALLED_APPS = [
    "ctf",
    "teamname",
    "files",
    "colorfield",
    "debug_toolbar",
    "crispy_forms",
    "crispy_bootstrap4",
    "django_extensions",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

MIDDLEWARE = [
    "csp.middleware.CSPMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "teamname.urls"
LOGIN_REDIRECT_URL = "dashboard"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "teamname.wsgi.application"

ADMINS = (("Minigrim0", "grimauflorent@gmail.com"),)

APPEND_SLASH = True
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    "default": env.db_url("DATABASE_URL", default=f"sqlite:///{BASE_DIR}/db.sqlite3")
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Europe/Brussels"
USE_I18N = True
USE_L10N = True
USE_TZ = True
CRISPY_TEMPLATE_PACK = "bootstrap4"

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static/"
STATICFILES_DIRS = (BASE_DIR / "teamname/assets",)

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media/"

HACKMD_ROOT_URL = env("HACKMDROOT", default="http://127.0.0.1")

CSP_IMG_SRC = (
    "'self'",
    "'unsafe-inline'",
    HACKMD_ROOT_URL,
    "https://placekitten.com",
    "https://www.gravatar.com",
    "https://getbootstrap.com",
)
CSP_STYLE_SRC = (
    "'self'",
    "'unsafe-inline'",
    HACKMD_ROOT_URL,
    "https://cdn.jsdelivr.net",
)
CSP_SCRIPT_SRC = (
    "'self'",
    "'unsafe-inline'",
    HACKMD_ROOT_URL,
    "https://cdn.jsdelivr.net",
    "http://ajax.googleapis.com",
)
CSP_DEFAULT_SRC = ("'self'", "'unsafe-inline'", HACKMD_ROOT_URL)
logger.info(f"HACKMD_ROOT_URL: {HACKMD_ROOT_URL}")

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
