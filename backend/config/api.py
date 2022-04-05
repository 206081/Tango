from rest_framework import routers

from apps.tables.views import TableViewSet
from apps.users.views import UserViewSet

# Settings
api = routers.DefaultRouter()
api.trailing_slash = "/?"

# Users API
api.register(r"users", UserViewSet)
api.register(r"tables", TableViewSet)
api.register(r"tables/(?P<pk>\w{0,50})", TableViewSet)
