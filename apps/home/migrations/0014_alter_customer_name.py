# Generated by Django 3.2.8 on 2021-11-04 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, verbose_name='نام'),
        ),
    ]
