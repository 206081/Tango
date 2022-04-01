from django.conf import settings
from django.db import models


class Table(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def pretty_str(self):
        return {"Id": self.pk, "Name": self.name}
