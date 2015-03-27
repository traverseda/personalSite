# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogEngine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='publishDate',
            field=models.DateTimeField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
