# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-29 05:31
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('slug', models.SlugField(max_length=150)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, upload_to='Product_photo')),
                ('manufacturer', models.CharField(blank=True, max_length=300)),
                ('Price_in_Rs', models.DecimalField(decimal_places=2, default=Decimal('0.0000'), max_digits=4)),
            ],
        ),
    ]
