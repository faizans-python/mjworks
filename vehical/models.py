from django.db import models
from django.contrib.auth.models import User

from customer.models import Customer


class Vehical(models.Model):

    """
    Customer model to store all customer related information
    """

    customer = models.ForeignKey(Customer)
    created_by = models.ForeignKey(User)
    vehical_number = models.CharField(blank=True, max_length=50)
    vehical_name = models.CharField(blank=True, max_length=50)
    vehical_colour = models.CharField(blank=True, max_length=50)
    about = models.TextField(blank=True, null=True)
    last_serviced_date = models.DateTimeField()

    def __unicode__(self):
        return u''.join((self.car_number))
