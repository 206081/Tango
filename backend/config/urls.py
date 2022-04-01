from django.urls import path
from django.contrib import admin
from django.contrib.auth import logout
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from django.conf.urls import include

from config.api import api


urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("logout/", logout, {"next_page": "/"}, name="logout"),
    path("api/", include(api.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
