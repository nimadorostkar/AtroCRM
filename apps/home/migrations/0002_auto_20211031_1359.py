# Generated by Django 3.2.8 on 2021-10-31 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='product_tag',
            field=models.ManyToManyField(blank=True, to='home.Product', verbose_name='تگ محصولی'),
        ),
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.BooleanField(default=True, verbose_name='موجود'),
        ),
        migrations.AlterField(
            model_name='order_req',
            name='status',
            field=models.CharField(choices=[('تکمیل شده', 'تکمیل شده'), ('لغو شده', 'لغو شده'), ('دریافت پیش پرداخت', 'دریافت پیش پرداخت'), ('پرداخت شده', 'پرداخت شده'), ('در حال بررسی', 'در حال بررسی')], default='در حال بررسی', max_length=30, verbose_name='وضعیت'),
        ),
    ]
