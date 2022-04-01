from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import Table
from .serializers import TableCreateSerializer, TableListSerializer


class TableViewSet(ViewSet):
    queryset = Table.objects.all()

    def create(self, request):
        data = request.data
        serializer = TableCreateSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def list(self, request):
        serializer = TableListSerializer()
        return Response(serializer.get_tables())
