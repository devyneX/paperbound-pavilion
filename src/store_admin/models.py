from django.db import models


# Thank you Dmitry and Jarett Millard
class DashboardPermissions(models.Model):

    class Meta:
        managed = False

        default_permissions = ()

        permissions = (('view_dashboard', 'Can view dashboard'),)
