from django.contrib import admin

from .models import Address, User

admin.site.register(User)
admin.site.register(Address)
