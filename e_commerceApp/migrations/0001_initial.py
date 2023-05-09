# Generated by Django 4.1.7 on 2023-05-09 10:29

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('houseNumber', models.PositiveSmallIntegerField(default=0)),
                ('street', models.CharField(default='', max_length=50)),
                ('city', models.CharField(default='', max_length=50)),
                ('country', models.CharField(default='', max_length=50)),
                ('postalCode', models.CharField(default='', max_length=50)),
            ],
            options={
                'db_table': 'address',
                'ordering': ['country', 'city'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('firstName', models.CharField(default='', max_length=50)),
                ('lastName', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(default='+21600000000', max_length=20)),
                ('birthdate', models.DateField(default=datetime.date(1995, 11, 11))),
            ],
            options={
                'db_table': 'client',
            },
        ),
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(default='', max_length=254)),
                ('phone', models.TextField(default='', max_length=20)),
                ('site_url', models.URLField(default='')),
            ],
            options={
                'db_table': 'provider',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='', max_length=20)),
                ('price', models.FloatField(default=0)),
                ('stock', models.PositiveSmallIntegerField(default=0)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image/product_image')),
                ('description', models.TextField(blank=True, null=True)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerceApp.provider')),
            ],
            options={
                'db_table': 'product',
                'ordering': ['label', '-price'],
            },
        ),
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_cmd', models.DateField(default=django.utils.timezone.now)),
                ('quality', models.PositiveSmallIntegerField(default=1)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerceApp.client')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_commerceApp.product')),
            ],
            options={
                'verbose_name': 'Command table',
                'db_table': 'command',
                'ordering': ['-date_cmd'],
                'unique_together': {('client', 'product', 'date_cmd')},
            },
        ),
        migrations.AddField(
            model_name='client',
            name='clientProduct',
            field=models.ManyToManyField(through='e_commerceApp.Command', to='e_commerceApp.product'),
        ),
    ]