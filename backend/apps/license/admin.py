from django.contrib import admin

from backend.apps.license.models import IssuingAuthority
from backend.apps.license.models import Region
from backend.apps.license.models import DBLicense
from backend.apps.license.models import CodeLicense


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    """ Модель Региона """

    list_display = ('title', 'is_active', 'created_date', 'updated')

@admin.register(IssuingAuthority)
class IssuingAuthorityAdmin(admin.ModelAdmin):
    """ Модель органа выдачи """

    list_display = ('title', 'is_active', 'created_date', 'updated')

@admin.register(CodeLicense)
class CodeLicenseAdmin(admin.ModelAdmin):
    """ Модель STATUS """

    list_display = ('title', 'is_active', 'created_date', 'updated')

@admin.register(DBLicense)
class DBLicenseAdmin(admin.ModelAdmin):
    """ Модель Базы лицензий """

    list_display = ('number_register', 'name_entity', 'is_active', 'created_date', 'updated')
