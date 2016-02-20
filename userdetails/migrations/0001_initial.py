# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('designation', models.CharField(max_length=120, blank=True)),
                ('about', models.TextField(null=True, blank=True)),
                ('gender', models.CharField(blank=True, max_length=20, choices=[(b'Female', b'FEMALE'), (b'Male', b'MALE')])),
                ('address', models.TextField(null=True, blank=True)),
                ('phone_number', models.IntegerField()),
                ('profile_picture', models.ImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('profile_picture_icon', django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('profile_picture_thumbnail', django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True)),
                ('profile_picture_macroicon', django_resized.forms.ResizedImageField(null=True, upload_to=b'profile_picture/', blank=True)),
            ],
        ),
    ]
