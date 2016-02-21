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
        del customer_form['radio1']
        customer = Customer.objects.filter(
            **customer_form)
        if not customer:
            customer_form['created_by'] = request.user
            customer_form['gender'] = gender
            customer_obj = Customer.objects.create(**customer_form)

        vehical_form['customer'] = customer_obj
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
        service_form['customer'] = customer_obj
        service_form['vehical'] = vehical
        service_form['expected_delivery_date'] = datetime.datetime.strptime(
            service_form['expected_delivery_date'], "%m/%d/%Y").date()
        service = Service.objects.create(**service_form)
        obj = list(Service.objects.filter(
            invoice_number=service.invoice_number).values())
        json.JSONEncoder.default = lambda self, obj: (
            obj.isoformat() if isinstance(obj, datetime.datetime) else None)
        return HttpResponse(json.dumps(obj), content_type="application/json")


@require_http_methods(["GET"])
@login_required(login_url='/')
def service_search(request):
    if request.method == "GET":
        context = RequestContext(request, {
            "services": Service.objects.filter(
                is_active=True).only("invoice_number",
                                     "customer",
                                     "vehical",
                                     "is_serviced",
                                     "service_date",
                                     "total_pending",
                                     "total_paid")})
        return render_to_response('service/servicesearch.html',
                                  context_instance=context)


@require_http_methods(["GET"])
@login_required(login_url='/')
def service_view(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(invoice_number=id)
        if service_obj:
            context = RequestContext(request, {
                "service": service_obj[0]})
            return render_to_response('service/viewservice.html',
                                      context_instance=context)
        return HttpResponseRedirect("/home/")


@require_http_methods(["GET"])
@login_required(login_url='/')
def service_pending(request):
    if request.method == "GET":
        context = RequestContext(request, {
            "services": Service.objects.filter(
                is_active=True, is_serviced=False)})
        return render_to_response('service/pendingservice.html',
                                  context_instance=context)
