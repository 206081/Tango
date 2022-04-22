# Generated by Django 3.2 on 2022-04-18 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='assignee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='assignee', to=settings.AUTH_USER_MODEL, verbose_name='Assignee'),
        ),
        migrations.AddField(
            model_name='list',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Registered at'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='list',
            unique_together={('name', 'table')},
        ),
    ]