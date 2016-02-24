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
from service.models import (
    Service,
    Payment
)
from parts.models import Part


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
        if customer_form.get('radio1'):
            del customer_form['radio1']
        customer = Customer.objects.filter(
            **customer_form)
        if not customer:
            customer_form['created_by'] = request.user
            customer_form['gender'] = gender
            customer_obj = Customer.objects.create(**customer_form)
        else:
            customer_obj = customer[0]

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


@require_http_methods(["GET", "POST"])
@login_required(login_url='/')
def service_edit(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(invoice_number=id)
        if service_obj:
            context = RequestContext(request, {
                "service": service_obj[0]})
            return render_to_response('service/editservice.html',
                                      context_instance=context)
        return HttpResponseRedirect("/home/")
    if request.method == "POST":
        return HttpResponse("EDit")


@require_http_methods(["GET"])
@login_required(login_url='/')
def invoice_get(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(invoice_number=id)
        if service_obj:
            context = RequestContext(request, {
                "service": service_obj[0]})
            return render_to_response('service/invoice.html',
                                      context_instance=context)
        return HttpResponseRedirect("/home/")
    if request.method == "POST":
        return HttpResponse("EDit")


@require_http_methods(["GET", "POST"])
@login_required(login_url='/')
def create_invoice(request):
    if request.method == "GET":
        service_objs = Service.objects.filter(
            is_serviced=False, is_active=True)
        context = RequestContext(request, {
            "services": service_objs})
        return render_to_response('service/invoicecreate.html',
                                  context_instance=context)

    if request.method == "POST":
        return HttpResponse("EDit")


@require_http_methods(["GET", "POST"])
@login_required(login_url='/')
def invoice(request):
    if request.method == "POST":
        request_dict = request.POST.dict()
        data = json.loads(request_dict.keys()[0])
        service_obj = Service.objects.filter(
            invoice_number=data.get('service_id'))
        if service_obj:
            service_obj = service_obj[0]
            if not service_obj.is_serviced:
                service_obj.is_serviced = True
                service_obj.labour_cost = data.get('labour_cost', 0)
                service_obj.tax = data.get('tax', 0)
                service_obj.total_cost = data['total_cost']
                service_obj.remark = data.get('remark', "")
                service_obj.next_service_date = datetime.datetime.strptime(
                    data.get('next_service_date'), "%m/%d/%Y").date()
                service_obj.delivery_date = timezone.now()
                service_obj.total_paid += int(data['total_paid'])
                payment = Payment.objects.create(payment_amount=data.get('total_paid'),
                                                 recieved_by=request.user)
                service_obj.total_pending = int(
                    data.get('total_cost')) - int(data['total_paid'])

                part_data = data.get('part_data')
                part_obj = []
                part_total_cost = 0
                for part in part_data:
                    if part.get('part_name') and part.get('price'):
                        obj = Part.objects.create(part_name=part.get('part_name'),
                                                  price=part.get('price'),
                                                  part_quantity=part.get(
                                                      'part_quantity'),
                                                  created_by=request.user)
                        part_total_cost += (int(obj.price)
                                            * int(obj.part_quantity))
                        part_obj.append(obj)
                service_obj.parts.add(*part_obj)
                service_obj.payment.add(payment)
                service_obj.part_cost = part_total_cost
                service_obj.save()
                return HttpResponse("EDit Complete")
            return HttpResponseRedirect("/home/")


@require_http_methods(["POST"])
@login_required(login_url='/')
def pending_payment(request):
    if request.method == "POST":
        request_dict = request.POST.dict()
        data = json.loads(request_dict.keys()[0])
        service_obj = Service.objects.filter(invoice_number=data.get('service_id'))
        if service_obj:
            service_obj = service_obj[0]
            if service_obj.is_serviced:
                pending_amount = service_obj.total_pending - data.get('pending_payment')
                payment = Payment.objects.create(payment_amount=data.get('pending_payment'),
                                                 recieved_by=request.user)
                if pending_amount == 0:
                    service_obj.complete_payment = True

                service_obj.total_paid += data.get('pending_payment')
                service_obj.total_pending = pending_amount
                service_obj.payment.add(payment)
                service_obj.save()
                return HttpResponse("Pending payment Complete") 
            return HttpResponseRedirect("/home/")


@require_http_methods(["GET"])
@login_required(login_url='/')
def invoice_view(request, id):
    if request.method == "GET":
        service_obj = Service.objects.filter(is_active=True, invoice_number=id)
        if service_obj:
            context = RequestContext(request, {
                "service": service_obj[0]})
            return render_to_response('service/invoicepdf.html',
                                      context_instance=context)
