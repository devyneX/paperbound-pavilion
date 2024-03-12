STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Static files directories
STATICFILES_DIRS = [BASE_DIR / 'static']  # type: ignore # noqa
MEDIA_ROOT = BASE_DIR / 'media'  # type: ignore # noqa

# Static root
STATIC_ROOT = 'staticfiles'
