from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .codes import (
    Code,
    Detail,
    Message,
)
from .models import Card, Table
from .serializers import (
    CardCreateSerializer,
    CardListSerializer,
    CommentCreateSerializer,
    ListCreateSerializer,
    ListListSerializer,
    TableCreateSerializer,
    TableListSerializer,
    TaskCreateSerializer,
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
        return Response(
            {
                "detail": Detail.table.create,
                "code": Code.table.create,
                "messages": [
                    {
                        "message": Message.table.create,
                    }
                ],
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    def list(self, request):
        modified_data = request.data.copy()
        serializer = TableListSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "detail": Detail.table.list,
                "code": Code.table.list,
                "messages": [
                    {
                        "message": Message.table.list,
                    }
                ],
                "data": serializer.get_tables(),
            },
        )

    def retrieve(self, request, pk):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, pk):
            return response

        modified_data["pk"] = pk
        serializer = TableListSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "detail": Detail.table.retrieve,
                "code": Code.table.retrieve,
                "messages": [
                    {
                        "message": Message.table.retrieve,
                    }
                ],
                "data": serializer.get_table(),
            },
        )

    def update(self, request, pk):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, pk):
            return response

        modified_data["pk"] = pk
        serializer = TableCreateSerializer(
            instance=Table.objects.get(id=pk),
            data=modified_data,
            context={"request": self.request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "detail": Detail.table.update,
                "code": Code.table.update,
                "messages": [
                    {
                        "message": Message.table.update,
                    }
                ],
                "data": serializer.data,
            },
        )

    def partial_update(self, request, pk):
        modified_data = {}

        if response := get_user_table(request.user, pk):
            return response

        instance = Table.objects.get(id=pk)

        modified_data["pk"] = pk
        modified_data["name"] = request.data.get("name", instance.name)
        modified_data["owner"] = request.data.get("owner", set(owner.pk for owner in instance.owner.get_queryset()))
        modified_data["members"] = request.data.get(
            "members", set(member.pk for member in instance.members.get_queryset())
        )
        modified_data["is_archive"] = request.data.get("is_archive", instance.is_archive)
        serializer = TableCreateSerializer(
            instance=instance,
            data=modified_data,
            context={"request": self.request},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "detail": Detail.table.partial_update,
                "code": Code.table.partial_update,
                "messages": [
                    {
                        "message": Message.table.partial_update,
                    }
                ],
                "data": serializer.data,
            },
        )

    def destroy(self, request, *args, **kwargs):
        pass

    @action(detail=True)
    def all_table(self, request, pk=None):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, pk):
            return response

        modified_data["pk"] = pk
        serializer = TableListSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "detail": Detail.table.all_table,
                "code": Code.table.all_table,
                "messages": [
                    {
                        "message": Message.table.all_table,
                    }
                ],
                "data": serializer.get_all_table(),
            },
        )

    @action(detail=False)
    def all_tables(self, request):
        modified_data = request.data.copy()

        serializer = TableListSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "detail": Detail.table.all_tables,
                "code": Code.table.all_tables,
                "messages": [
                    {
                        "message": Message.table.all_tables,
                    }
                ],
                "data": serializer.get_all_tables(),
            },
        )


class ListViewSet(ViewSet):
    def create(self, request, table_pk=None):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["table"] = table_pk
        serializer = ListCreateSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "detail": Detail.list.create,
                "code": Code.list.create,
                "messages": [
                    {
                        "message": Message.list.create,
                    }
                ],
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    def list(self, request, table_pk=None):
        modified_data = self.request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["table"] = table_pk
        serializer = ListListSerializer(data=modified_data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "detail": Detail.list.list,
                "code": Code.list.list,
                "messages": [
                    {
                        "message": Message.list.list,
                    }
                ],
                "data": serializer.get_lists(),
            },
        )

    def retrieve(self, request, pk, table_pk=None):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["pk"] = pk
        modified_data["table"] = table_pk
        serializer = ListListSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "detail": Detail.list.retrieve,
                "code": Code.list.retrieve,
                "messages": [
                    {
                        "message": Message.list.retrieve,
                    }
                ],
                "data": serializer.get_list(),
            },
        )

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
        return Response(
            {
                "detail": Detail.card.create,
                "code": Code.card.create,
                "messages": [
                    {
                        "message": Message.card.create,
                    }
                ],
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    def list(self, request, table_pk=None, list_pk=None):
        modified_data = self.request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["list"] = list_pk
        serializer = CardListSerializer(data=modified_data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "detail": Detail.card.list,
                "code": Code.card.list,
                "messages": [
                    {
                        "message": Message.card.list,
                    }
                ],
                "data": serializer.get_cards(),
            },
        )

    def retrieve(self, request, pk, table_pk=None, list_pk=None):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["pk"] = pk
        modified_data["list"] = list_pk
        serializer = CardListSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        return Response(
            {
                "detail": Detail.card.retrieve,
                "code": Code.card.retrieve,
                "messages": [
                    {
                        "message": Message.card.retrieve,
                    }
                ],
                "data": serializer.get_card(),
            },
        )

    def update(self, request, pk, table_pk=None, list_pk=None):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["pk"] = pk
        modified_data["list"] = list_pk
        serializer = CardCreateSerializer(
            instance=Card.objects.get(id=pk), data=modified_data, context={"request": self.request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "detail": Detail.card.update,
                "code": Code.card.update,
                "messages": [
                    {
                        "message": Message.card.update,
                    }
                ],
                "data": serializer.data,
            },
        )

    def partial_update(self, request, pk, table_pk=None, list_pk=None):
        modified_data = {}

        if response := get_user_table(request.user, table_pk):
            return response

        instance = Card.objects.get(id=pk)

        modified_data["pk"] = pk
        modified_data["list"] = list_pk
        modified_data["name"] = request.data.get("name", instance.name)
        modified_data["description"] = request.data.get("description", instance.description)
        serializer = CardCreateSerializer(instance=instance, data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                "detail": Detail.card.partial_update,
                "code": Code.card.partial_update,
                "messages": [
                    {
                        "message": Message.card.partial_update,
                    }
                ],
                "data": serializer.data,
            },
        )

    def destroy(self, request, *args, **kwargs):
        pass


class CommentViewSet(ViewSet):
    def create(self, request, table_pk=None, list_pk=None, card_pk=None):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response

        modified_data["list"] = list_pk
        modified_data["card"] = card_pk
        modified_data["author"] = self.request.user.id
        serializer = CommentCreateSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "detail": Detail.comment.create,
                "code": Code.comment.create,
                "messages": [
                    {
                        "message": Message.comment.create,
                    }
                ],
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    def list(self, request, table_pk=None, list_pk=None, card_pk=None):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass


class TaskViewSet(ViewSet):
    def create(self, request, table_pk=None, list_pk=None, card_pk=None):
        modified_data = request.data.copy()

        if response := get_user_table(request.user, table_pk):
            return response
        print("in task view")
        modified_data["list"] = list_pk
        modified_data["card"] = card_pk
        serializer = TaskCreateSerializer(data=modified_data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                "detail": Detail.task.create,
                "code": Code.task.create,
                "messages": [
                    {
                        "message": Message.task.create,
                    }
                ],
                "data": serializer.data,
            },
            status=status.HTTP_201_CREATED,
        )

    def list(self, request, *args, **kwargs):
        pass

    def retrieve(self, request, *args, **kwargs):
        pass

    def update(self, request, *args, **kwargs):
        pass

    def destroy(self, request, *args, **kwargs):
        pass
