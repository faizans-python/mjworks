# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('mechanic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=b'profile_picture/', blank=True),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='profile_picture_icon',
            field=django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='profile_picture_macroicon',
            field=django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True),
        ),
        migrations.AddField(
            model_name='mechanic',
            name='profile_picture_thumbnail',
            field=django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True),
        ),
    ]
