from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path
from ninja import NinjaAPI

from backend.apps.license.views import router as license_router
from backend.apps.account.auth.login import router as login_router
from backend.config import settings

api = NinjaAPI(
    title="БАЗА ЛИЦЕНЗИИ 🔥",
    version="1.0.0",
)

api.add_router(
    "api/",
    license_router,
    tags=["База лицензии"]
)

api.add_router(
    "api/",
    login_router,
    tags=["ВХОД"]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

