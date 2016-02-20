# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20160218_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='gender',
            field=models.CharField(blank=True, max_length=20, null=True, choices=[(b'Female', b'FEMALE'), (b'Male', b'MALE')]),
        ),
    ]
