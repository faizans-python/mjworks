# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('about', models.TextField(null=True, blank=True)),
                ('address', models.TextField(null=True, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('phone_number', models.IntegerField()),
                ('total_paid', models.IntegerField(default=0)),
                ('total_pending', models.IntegerField(default=0)),
                ('profile_picture', models.ImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('profile_picture_icon', django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('profile_picture_thumbnail', django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('profile_picture_macroicon', django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True)),
            ],
        ),
    ]
