# Generated by Django 2.2 on 2020-02-17 08:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, max_length=220, null=True)),
                ('session_key', models.CharField(blank=True, max_length=100, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('ended', models.BooleanField(default=False)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
