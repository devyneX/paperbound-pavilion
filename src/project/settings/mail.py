EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'paperboundpavilion@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')  # type: ignore # noqa
EMAIL_ATTACHMENT_PATH = '/tmp'
