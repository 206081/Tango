from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Card, List, Table
from .serializers import TableCreateSerializer, TableListSerializer


class TableViewSet(ViewSet):
    queryset = Table.objects.all()

    def create(self, request):
        data = request.data.copy()
        data["owner"] = request.user.id
        serializer = TableCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):

        context = {"request": self.request}
        if "pk" in self.kwargs:
            modified_data = self.request.data.copy()
            modified_data["pk"] = self.kwargs.get("pk")
            modified_data["owner"] = request.user.id
            kwargs["data"] = modified_data
            serializer = TableListSerializer(data=modified_data, context=context)
            serializer.is_valid(raise_exception=True)

            return Response(serializer.get_table())

        serializer = TableListSerializer(data={"owner": request}, context=context)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.get_tables())


class ListViewSet(ViewSet):
    queryset = List.objects.all()


class ClassViewSet(ViewSet):
    queryset = Card.objects.all()
