from django.db import models
from django.utils.translation import gettext_lazy as _


class SoftDeletionManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('created_at'))
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name=_('deleted_at'))
    deleted = models.BooleanField(default=False,
                                  verbose_name=_('deleted'))

    objects = SoftDeletionManager()
    all_objects = models.Manager(
    )  # Manager to access all objects, including soft-deleted ones

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()

    def hard_delete(self):
        super().delete()

    class Meta:
        abstract = True
