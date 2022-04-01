from django.conf import settings
from django.db.models import Q
from rest_framework import serializers

from ..tables.models import Table
from ..users.models import User


class TableCreateSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = Table
        fields = ("id", "name")


class TableListSerializer(serializers.ModelSerializer):
    def get_tables(self):
        return [p.pretty_str() for p in Table.objects.all()]

    class Meta:
        model = Table
        fields = ("id",)
