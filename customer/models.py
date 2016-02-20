from enum import Enum

from django.db import models
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver

from django_resized import ResizedImageField


class Customer(models.Model):

    """
    Customer model to store all customer related information
    """
    class Gender(Enum):

        """
        This class creates enum for gender field of UserProfile.
        """

        MALE = 'Male'
        FEMALE = 'Female'

        @classmethod
        def as_tuple(cls):
            return ((item.value, item.name.replace('_', ' ')) for item in cls)

    first_name = models.CharField(blank=True, max_length=50)
    last_name = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    phone_number = models.CharField(max_length=50)
    total_paid = models.IntegerField(default=0)
    total_pending = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    gender = models.CharField(blank=True, null=True, max_length=20,
                              choices=Gender.as_tuple())
    profile_picture = models.ImageField(
        upload_to='profile_picture/',
        blank=True,
        null=True
    )
    profile_picture_icon = ResizedImageField(
        size=[20, 20],
        quality=100,
        crop=['middle', 'center'],
        upload_to='profile_picture/',
        blank=True,
        null=True
    )
    profile_picture_thumbnail = ResizedImageField(
        size=[300, 200],
        quality=100,
        upload_to='profile_picture/',
        blank=True,
        null=True
    )
    profile_picture_macroicon = ResizedImageField(
        size=[50, 50],
        quality=100,
        crop=['middle', 'center'],
        upload_to='profile_picture/',
        blank=True,
        null=True
    )

    def __unicode__(self):
        return u' '.join((self.first_name, self.last_name))
