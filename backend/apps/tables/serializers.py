from django.db.models import Q
from rest_framework import serializers

from ..tables.models import Table
from ..users.models import User


class TableCreateSerializer(serializers.ModelSerializer):

    name = serializers.CharField(max_length=100, required=True)
    members = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.filter(is_active=True),
        required=False,
    )

    class Meta:
        model = Table
        fields = ("id", "owner", "name", "members")


class TableListSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    pk = serializers.IntegerField(required=False)

    def get_table(self):
        return [
            p.pretty_str()
            for p in Table.objects.filter(
                (Q(owner=self.validated_data["owner"].pk) | Q(members__id=self.validated_data["owner"].pk))
                & Q(pk=self.validated_data["pk"])
            )
        ]

    def get_tables(self):
        return [
            p.pretty_str()
            for p in Table.objects.filter(
                Q(owner=self.validated_data["owner"].pk) | Q(members__id=self.validated_data["owner"].pk)
            )
        ]

    class Meta:
        model = Table
        fields = ("owner", "pk")
