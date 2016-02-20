# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20160220_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='labour_cost',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='part_cost',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='total_cost',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
