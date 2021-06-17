from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models as core_models
from django.db.models.base import ModelBase

# class UserAdmin(BaseUserAdmin):
#     ordering = ['id']

for name, var in core_models.__dict__.items():
    if type(var) is ModelBase and name != 'AbstractBaseUser' and name != 'PermissionsMixin':
        admin.site.register(var)
# admin.site.register(core_models.AuthUser, UserAdmin)