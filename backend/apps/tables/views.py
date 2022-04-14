from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .serializers import (
    CardCreateSerializer,
    CardListSerializer,
    ListCreateSerializer,
    ListListSerializer,
    TableCreateSerializer,
    TableListSerializer,
    get_user_table,
)


class TableViewSet(ViewSet):
    def create(self, request):

        modified_data = request.data.copy()
        modified_data["owner"] = set(modified_data.get("owner", ()))
        modified_data["owner"].add(self.request.user.id)
        modified_data["members"] = set(modified_data.get("members", ()))
        modified_data["members"].update(modified_data["owner"])

        serializer = TableCreateSerializer(data=modified_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def list(self, request):
        modified_data = request.data.copy()
        serializer = TableListSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.get_tables())

    def retrieve(self, request, pk):
        modified_data = request.data.copy()
        modified_data["pk"] = pk
        serializer = TableListSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.get_table())

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass


class ListViewSet(ViewSet):
    def create(self, request, table_pk=None):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["table"] = table_pk
        serializer = ListCreateSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def list(self, request, table_pk=None):
        modified_data = self.request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["table"] = table_pk
        serializer = ListListSerializer(data=modified_data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.get_lists())

    def retrieve(self, request, pk, table_pk=None):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["pk"] = pk
        modified_data["table"] = table_pk
        serializer = ListListSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.get_list())

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass


class CardViewSet(ViewSet):
    def create(self, request, table_pk=None, list_pk=None):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["list"] = list_pk
        serializer = CardCreateSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def list(self, request, table_pk=None, list_pk=None):
        modified_data = self.request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["list"] = list_pk
        serializer = CardListSerializer(data=modified_data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.get_cards())

    def retrieve(self, request, pk, table_pk=None, list_pk=None):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["pk"] = pk
        modified_data["list"] = list_pk
        serializer = CardListSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.get_card())

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass
