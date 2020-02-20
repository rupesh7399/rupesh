# Generated by Django 2.2 on 2020-02-20 08:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='Inspect',
        ),
        migrations.AddField(
            model_name='task',
            name='Inspect',
            field=models.ManyToManyField(blank=True, null=True, related_name='Inspect', to=settings.AUTH_USER_MODEL),
        ),
    ]
