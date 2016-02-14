from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField

from customer.models import Customer
from parts.models import Part
from mechanic.models import Mechanic
from vehical.models import Vehical


class Service(models.Model):

    """
    Service model to store all service related information
    """

    customer = models.ForeignKey(Customer)
    serviced_by = models.ForeignKey(Mechanic)
    created_by = models.ForeignKey(User)
    vehical = models.ForeignKey(Vehical)
    parts = models.ManyToManyField(Part)
    remark = models.TextField(blank=True, null=True)
    service_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    total_paid = models.IntegerField(default=0)
    total_pending = models.IntegerField(default=0)
    next_service_date = models.DateTimeField()
    invoice_number = models.AutoField(primary_key=True)
    recipient_name = models.CharField(blank=True, max_length=50)
    recipient_nuber = models.IntegerField()
    labour_cost = models.IntegerField()
    part_cost = models.IntegerField()
    total_cost = models.IntegerField()

    def __unicode__(self):
        return u''.join((self.invoice_number))
