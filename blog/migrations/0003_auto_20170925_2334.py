# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 23:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=tinymce.models.HTMLField(blank=True, help_text='Enter a short description.', null=True),
        ),
    ]
