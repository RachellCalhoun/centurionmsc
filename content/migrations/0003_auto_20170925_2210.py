# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 22:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20170925_1932'),
    ]

    operations = [
        migrations.RenameField(
            model_name='header',
            old_name='backgroun_image',
            new_name='background_image',
        ),
    ]
