# Generated by Django 2.2 on 2020-02-10 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(on_delete=False, to='carts.Cart'),
        ),
    ]
