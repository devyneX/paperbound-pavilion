from django.utils.translation import gettext_lazy as _

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Static files directories
STATICFILES_DIRS = [BASE_DIR / 'static']  # type: ignore # noqa
MEDIA_ROOT = BASE_DIR / 'media'  # type: ignore # noqa

# Static root
STATIC_ROOT = 'staticfiles'

LOGIN_REDIRECT_URL = '/'

# cache
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}


LANGUAGES = (
    ('en', _('English')),
    ('bn', _('Bangla')),
)
LOCALE_PATHS = [
    BASE_DIR / 'locale/',  # type: ignore # noqa
]
