# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20160218_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='expected_delivery_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='next_service_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
