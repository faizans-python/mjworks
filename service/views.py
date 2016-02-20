import json
import datetime

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.http import (
    HttpResponse,
    HttpResponseBadRequest
)
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import timezone

from mechanic.models import Mechanic
from customer.models import Customer
from vehical.models import Vehical
from service.models import Service


@require_http_methods(["GET"])
@login_required(login_url='/')
def service_add(request):
    if request.method == "GET":
        context = RequestContext(request, {
            "customers": Customer.objects.filter(is_active=True),
            "mechanics": Mechanic.objects.filter(is_active=True)})
        return render_to_response('service/service.html',
                                  context_instance=context)


@require_http_methods(["POST"])
@login_required(login_url='/')
def service_create(request):
    if request.method == "POST":
        data = request.POST.dict()
        forms = json.loads(data.keys()[0])
        customer_form = forms.get('customer')
        vehical_form = forms.get('vehical')
        service_form = forms.get('service_deatils')
        mechanic_id = forms.get('mechanic')
        gender = forms.get('gender')
        customer, customer_status = Customer.objects.get_or_create(
            **customer_form)
        if customer_status:
            customer.gender = gender
            customer.save()

        vehical_form['customer'] = customer
        vehical = Vehical.objects.filter(**vehical_form)
        if not vehical:
            vehical_form['created_by'] = request.user
            vehical_form['last_serviced_date'] = timezone.now()
            vehical = Vehical.objects.create(**vehical_form)
        else:
            vehical = vehical[0]
            vehical.last_serviced_date = timezone.now()
            vehical.save()

        if mechanic_id:
            service_form['serviced_by'] = Mechanic.objects.get(id=mechanic_id)
        service_form['created_by'] = request.user
        service_form['customer'] = customer
        service_form['vehical'] = vehical
        service_form['expected_delivery_date'] = datetime.datetime.strptime(
            service_form['expected_delivery_date'], "%m/%d/%Y").date()
        service = Service.objects.create(**service_form)
        obj = list(Service.objects.filter(
            invoice_number=service.invoice_number).values())
        json.JSONEncoder.default = lambda self, obj: (
            obj.isoformat() if isinstance(obj, datetime.datetime) else None)
        return HttpResponse(json.dumps(obj), content_type="application/json")
