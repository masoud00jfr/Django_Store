# Generated by Django 3.2.7 on 2021-09-10 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70, verbose_name='نام دسته')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70, verbose_name='نام محصول')),
                ('description', models.TextField(blank=True, null=True, verbose_name='معرفی محصول')),
                ('stock', models.PositiveIntegerField(default=1, verbose_name='موجودی کالا')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='قیمت')),
                ('pub_date', models.DateField(auto_now_add=True, verbose_name='تاریخ انتشار')),
                ('is_active', models.BooleanField(default=True, verbose_name='در دسترس')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='products.category', verbose_name='دسته بندی')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='products')),
                ('is_main', models.BooleanField(default=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]