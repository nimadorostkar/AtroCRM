# Generated by Django 3.2.8 on 2021-11-04 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20211105_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='توضیحات'),
        ),
    ]