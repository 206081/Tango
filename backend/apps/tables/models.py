from django.conf import settings
from django.db import models


class Table(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    owner = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Owner", blank=False, related_name="owner")
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, verbose_name="Member", related_name="members")
    is_archive = models.BooleanField(verbose_name="Archive", default=False)

    def __str__(self):
        return self.name

    def pretty_str(self):
        return {
            "Id": self.pk,
            "Name": self.name,
            "owner": [u.email for u in self.owner.all()],
            "members": [u.email for u in self.members.all()],
        }


class List(models.Model):
    name = models.CharField(verbose_name="Name", max_length=100)
    table = models.ForeignKey(Table, verbose_name="Table", on_delete=models.CASCADE, blank=False, related_name="table")
    is_archive = models.BooleanField(verbose_name="Archive", default=False)

    def __str__(self):
        return self.name

    def pretty_str(self):
        return {
            "Id": self.pk,
            "Name": self.name,
            "Table": self.table,
            "Archive": self.is_archive,
        }


class Card(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    description = models.TextField(verbose_name="Description", max_length=1024)
    list = models.ForeignKey(List, verbose_name="List", on_delete=models.CASCADE, blank=False, related_name="list")
    is_archive = models.BooleanField(verbose_name="Archive", default=False)

    def __str__(self):
        return self.name

    def pretty_str(self):
        return {
            "Id": self.pk,
            "Name": self.name,
            "Description": self.description,
            "List": self.list,
            "Archive": self.is_archive,
        }
