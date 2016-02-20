# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('parts', '0001_initial'),
        ('vehical', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0001_initial'),
        ('mechanic', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('remark', models.TextField(null=True, blank=True)),
                ('service_date', models.DateTimeField(auto_now_add=True)),
                ('delivery_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('total_paid', models.IntegerField(default=0)),
                ('total_pending', models.IntegerField(default=0)),
                ('next_service_date', models.DateTimeField()),
                ('invoice_number', models.AutoField(serialize=False, primary_key=True)),
                ('recipient_name', models.CharField(max_length=50, blank=True)),
                ('recipient_nuber', models.IntegerField()),
                ('labour_cost', models.IntegerField()),
                ('part_cost', models.IntegerField()),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('parts', models.ManyToManyField(to='parts.Part')),
                ('serviced_by', models.ForeignKey(to='mechanic.Mechanic')),
                ('vehical', models.ForeignKey(to='vehical.Vehical')),
            ],
        ),
    ]
