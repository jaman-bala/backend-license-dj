from django.contrib import admin

from backend.apps.account.models import UserProfile


admin.site.register(UserProfile)