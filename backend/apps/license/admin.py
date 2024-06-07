from django.contrib import admin

from backend.apps.license.models import IssuingAuthority
from backend.apps.license.models import Region


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_date', 'updated')

@admin.register(IssuingAuthority)
class IssuingAuthorityAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_date', 'updated')
