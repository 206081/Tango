from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from rest_framework import serializers, status
from rest_framework.response import Response

from ..tables.models import Card, List, Table
from ..users.models import User

IS_NOT_ARCHIVE = Q(is_archive=False)
IS_ARCHIVE = Q(is_archive=True)


def get_user_table(user, table_id):
    try:
        table = Table.objects.get(Q(pk=table_id) & IS_NOT_ARCHIVE)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        table = Table.objects.get(Q(members__id=user.id) & Q(pk=table_id) & IS_NOT_ARCHIVE)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_403_FORBIDDEN)


def get_user_tables(user):
    return Table.objects.filter((Q(members__id=user.id)) & IS_NOT_ARCHIVE)


class TableCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    owner = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.filter(is_active=True),
        required=False,
    )
    members = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=User.objects.filter(is_active=True),
        required=False,
    )

    class Meta:
        model = Table
        fields = ("id", "owner", "name", "members")


class TableListSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    pk = serializers.IntegerField(required=False)

    def get_table(self):
        table = Table.objects.filter(
            Q(members__id=self.validated_data["user"].pk) & Q(pk=self.validated_data["pk"]) & IS_NOT_ARCHIVE
        )
        return table[0].get_details() if table else []

    def get_tables(self):
        return [p.get_general_info() for p in get_user_tables(self.validated_data["user"]).order_by("pk")]

    class Meta:
        model = Table
        fields = ("user", "pk")


class ListCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = List
        fields = ("id", "name", "table")


class ListListSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(required=False)

    def get_list(self):
        return List.objects.get(Q(id=self.validated_data["pk"]) & IS_NOT_ARCHIVE).pretty_str()

    def get_lists(self):
        return [
            _list.pretty_str()
            for _list in List.objects.filter(Q(table_id=self.validated_data["table"].pk) & IS_NOT_ARCHIVE)
        ]

    class Meta:
        model = List
        fields = ("pk", "table")


class CardCreateSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    description = serializers.CharField(max_length=1024, required=False)

    class Meta:
        model = Card
        fields = ("id", "name", "description", "list")


class CardListSerializer(serializers.ModelSerializer):
    pk = serializers.IntegerField(required=False)

    def get_card(self):
        return Card.objects.get(Q(id=self.validated_data["pk"]) & IS_NOT_ARCHIVE).pretty_str()

    def get_cards(self):
        return [
            card.pretty_str()
            for card in Card.objects.filter(Q(list_id=self.validated_data["list"].pk) & IS_NOT_ARCHIVE)
        ]

    class Meta:
        model = Card
        fields = ("pk", "list")
