# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 14:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pharmacy', '0001_initial'),
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sells',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price_per_item', models.FloatField()),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.item')),
                ('pharmacy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacy.pharmacy')),
            ],
        ),
    ]
