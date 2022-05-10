from rest_framework_nested import routers

from apps.tables.views import CardViewSet, CommentViewSet, ListViewSet, TableViewSet
from apps.users.views import UserViewSet

# Settings
router = routers.DefaultRouter()
router.trailing_slash = "/?"

# Users API
router.register(r"users", UserViewSet)
router.register(r"tables", TableViewSet, basename="tables")

tables_router = routers.NestedSimpleRouter(router, r"tables", lookup="table")
tables_router.register(r"lists", ListViewSet, basename="lists")

lists_router = routers.NestedSimpleRouter(tables_router, r"lists", lookup="list")
lists_router.register(r"cards", CardViewSet, basename="cards")

cards_router = routers.NestedSimpleRouter(lists_router, r"cards", lookup="card")
cards_router.register(r"comments", CommentViewSet, basename="comments")
