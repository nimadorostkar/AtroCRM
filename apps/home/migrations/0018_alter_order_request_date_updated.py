# Generated by Django 3.2.9 on 2021-11-15 23:34

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_order_request_date_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_request',
            name='date_updated',
            field=django_jalali.db.models.jDateTimeField(auto_now_add=True, verbose_name='آخرین ویرایش'),
        ),
    ]
