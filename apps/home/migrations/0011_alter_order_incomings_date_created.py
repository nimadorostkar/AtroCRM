# Generated by Django 3.2.8 on 2021-11-02 23:01

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_order_incomings_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_incomings',
            name='date_created',
            field=django_jalali.db.models.jDateField(verbose_name='تاریخ'),
        ),
    ]
