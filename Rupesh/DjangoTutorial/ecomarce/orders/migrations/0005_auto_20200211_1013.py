# Generated by Django 2.2 on 2020-02-11 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_billing_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='billing.BillingProfile'),
        ),
    ]
