# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehical', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehical',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='vehical',
            name='last_serviced_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='vehical',
            name='vehical_number',
            field=models.CharField(unique=True, max_length=50),
        ),
    ]
