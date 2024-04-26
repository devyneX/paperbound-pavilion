from django.conf import settings
from django.utils.translation import gettext as _


def environment_callback(request):
    if settings.DEBUG:
        return [_('Development'), 'info']

    return [_('Production'), 'warning']
