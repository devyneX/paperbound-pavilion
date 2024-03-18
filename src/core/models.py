from django.db import models


class SoftDeletionManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

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
