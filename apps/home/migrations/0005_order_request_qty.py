# Generated by Django 3.2.8 on 2021-10-31 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_customer_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_request',
            name='qty',
            field=models.IntegerField(default='1', verbose_name='تعداد'),
        ),
    ]