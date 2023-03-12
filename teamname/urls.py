from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import teamname.views as views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("admin/", admin.site.urls),
    path("ctf/", include("ctf.urls")),
    path("", views.home, name="dashboard"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
