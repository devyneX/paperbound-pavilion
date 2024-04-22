import json

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    @staticmethod
    def extract_roles(file):
        with open(file, 'r') as f:
            roles = json.load(f)
        return roles

    def create_group(self, role):
        self.stdout.write(f'Creating Role {role}...')
        group, created = Group.objects.get_or_create(name=role)
        if created:
            self.stdout.write(f'Role {role} created')
        else:
            self.stdout.write(f'Role {role} already exists')

        return group

    @staticmethod
    def get_permission_objects(permissions):
        permission_objects = []
        for permission in permissions:
            app, model = permission['content_type'].split(' | ')
            app = app.lower().replace(' ', '')
            model = model.lower().replace(' ', '')
            content_type = ContentType.objects.get(app_label=app, model=model)
            permission_obj = Permission.objects.get(
                content_type=content_type, codename=permission['codename']
            )
            permission_objects.append(permission_obj)

        return permission_objects

    def _add_permissions(self, role, permissions):
        role.permissions.clear()
        for permission in permissions:
            role.permissions.add(permission)
            self.stdout.write(f'{permission} added to {role}')

    def add_permissions(self, role, permissions):
        if isinstance(permissions, str) and permissions == '__all__':
            permissions = Permission.objects.all()
            self._add_permissions(role, permissions)
            return

        permissions = self.get_permission_objects(permissions)

        self._add_permissions(role, permissions)

    def handle(self, *args, **options):
        self.stdout.write('Adding default roles...')
        roles = self.extract_roles(options['file'])
        for role, permissions in roles.items():
            group = self.create_group(role)
            self.add_permissions(group, permissions)

        self.stdout.write('Default roles added successfully')
