# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-26 02:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0013_auto_20160322_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='vote',
            field=models.CharField(choices=[('+1', '+1 (strong accept)'), ('+0', '+0 (weak accept)'), ('-0', '-0 (weak reject)'), ('-1', '-1 (strong reject)')], help_text='Your vote to accept or reject this talk. More information about the scoring and acceptance criteria can be found at the google doc <a href="https://goo.gl/EPlUZx" target="_blank">Review Guideline</a>.', max_length=2, verbose_name='vote'),
        ),
    ]
