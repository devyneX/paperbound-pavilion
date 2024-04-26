UNFOLD = {
    'SITE_URL': '/djadmin',
    'SHOW_HISTORY': True,  # show/hide 'History' button, default: True
    'SHOW_VIEW_ON_SITE': True,
    # show/hide 'View on site' button, default: True
    'ENVIRONMENT': 'src.djadmin_customization.utils.environment_callback',
    'DASHBOARD_CALLBACK': 'src.djadmin_customization.views.dashboard_callback',
    # 'THEME': 'dark',
    'SIDEBAR': {
        'show_search': True,  # Search in applications and models names
        'show_all_applications': True,
    },
}


def badge_callback(request):
    return 3


def permission_callback(request):
    return request.user.has_perm('sample_app.change_model')
