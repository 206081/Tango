from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.users.views import LogoutViewSet
from config.api import cards_router, lists_router, router, tables_router

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("api/", include(router.urls)),
    path("api/", include(tables_router.urls)),
    path("api/", include(lists_router.urls)),
    path("api/", include(cards_router.urls)),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/logout/", LogoutViewSet.as_view(), name="logout_user"),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
