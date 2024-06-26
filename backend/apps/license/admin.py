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

    list_display = ('number_register', 'name_entity', 'is_active', 'created_date', 'updated', 'created_by', 'updated_by')
    readonly_fields = ('created_by', 'updated_by')

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Если это новая запись
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)
