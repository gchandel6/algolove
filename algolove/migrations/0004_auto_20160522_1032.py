# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 05:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algolove', '0003_auto_20160517_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algo_snippet',
            name='pub_date',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='algo_snippet',
            name='updated_date',
            field=models.DateField(editable=False),
        ),
    ]