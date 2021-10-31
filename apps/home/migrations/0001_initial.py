# Generated by Django 3.2.8 on 2021-10-31 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='نام')),
                ('phone', models.CharField(max_length=200, null=True, verbose_name='تلفن')),
                ('additional_information', models.TextField(blank=True, max_length=1000, null=True, verbose_name='اطلاعات تکمیلی')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='تاریخ')),
            ],
        ),
        migrations.CreateModel(
            name='Order_req',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='توضیحات')),
                ('discount', models.IntegerField(default='0', verbose_name='درصد تخفیف')),
                ('status', models.CharField(choices=[('تکمیل شده', 'تکمیل شده'), ('لغو شده', 'لغو شده'), ('دریافت پیش پرداخت', 'دریافت پیش پرداخت'), ('پرداخت شده', 'پرداخت شده'), ('در حال بررسی', 'در حال بررسی')], default='در حال بررسی', max_length=20, verbose_name='وضعیت')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='تاریخ')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.customer', verbose_name='خریدار')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کارشناس فروش')),
            ],
            options={
                'verbose_name': 'سفارش',
                'verbose_name_plural': 'سفارشات',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, verbose_name='نام')),
                ('price', models.FloatField(null=True, verbose_name='قیمت ( ریال )')),
                ('description', models.TextField(blank=True, max_length=900, null=True, verbose_name='توضیحات')),
                ('image', models.ImageField(blank=True, default='media/Default.png', null=True, upload_to='media', verbose_name='تصویر')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='تاریخ')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='Order_steps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step', models.CharField(choices=[('اول', 'اول'), ('دوم', 'دوم'), ('سوم', 'سوم'), ('چهارم', 'چهارم'), ('پنجم', 'پنجم'), ('ششم', 'ششم'), ('هفتم', 'هفتم'), ('هشتم', 'هشتم'), ('نهم', 'نهم'), ('دهم', 'دهم')], max_length=20, verbose_name='گام')),
                ('description', models.TextField(blank=True, max_length=1000, null=True, verbose_name='توضیحات')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='تاریخ')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.order_req', verbose_name='برای سفارش')),
            ],
            options={
                'verbose_name': 'مرحله سفارش',
                'verbose_name_plural': 'مراحل سفارش',
            },
        ),
    ]
