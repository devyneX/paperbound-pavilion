import os  # noqa
from pathlib import Path

from split_settings.tools import include

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

include('base.py',)
include('app.py')
include('sslcommerz.py')
include('celery.py')
include('mail.py')
