from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import Group


class UserManager(BaseUserManager):

    def create(self, username, email, password, **extra_fields):
        user = super().create_user(
            username=username, email=email, password=password, **extra_fields
        )
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if not user.is_superuser:
            group = Group.objects.get(name='base_user')
            user.groups.add(group)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        if extra_fields.get('is_active') is not True:
            raise ValueError('Superuser must have is_active=True')

        return self.create_user(username, email, password, **extra_fields)


class CustomerManager(UserManager):

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_staff=False)
        return queryset


class StaffManager(UserManager):

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_staff=True)
        return queryset
