# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 22:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20170925_2218'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carousel_Image',
            new_name='CarouselImage',
        ),
    ]
