# Generated by Django 3.2.9 on 2021-11-15 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_order_request_date_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_request',
            name='date_updated',
        ),
    ]