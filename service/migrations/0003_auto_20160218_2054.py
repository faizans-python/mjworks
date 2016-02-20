# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_service_total_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='expected_delivery_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='service',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='service',
            name='is_archive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='service',
            name='delivery_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='recipient_nuber',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='serviced_by',
            field=models.ForeignKey(blank=True, to='mechanic.Mechanic', null=True),
        ),
    ]
