# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-22 05:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('algolove', '0004_auto_20160522_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coding_snippet',
            name='pub_date',
            field=models.DateField(editable=False),
        ),
        migrations.AlterField(
            model_name='coding_snippet',
            name='updated_date',
            field=models.DateField(editable=False),
        ),
    ]
