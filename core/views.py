from datetime import datetime

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.shortcuts import render_to_response

from service.models import Service
from customer.models import Customer


def index(request):
    return render(request, 'core/login.html')


@login_required(login_url='/')
def home(request):
    current_month = datetime.now().month
    context = RequestContext(request, {
        "pending_service": Service.objects.filter(is_active=True,
                                                  is_serviced=False),
        "total_service": len(Service.objects.filter(is_active=True,
                                                    is_serviced=True)),
        "total_customer": len(Customer.objects.filter(is_active=True)),
        "monthly_service": len(Service.objects.filter(service_date__month=current_month,
                                                      is_active=True,
                                                      is_serviced=True))})
    return render_to_response('core/context.html',
                              context_instance=context)

def page_not_found(request):
    return render(request, 'core/page_not_found.html')


@require_http_methods(["POST"])
def verify(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            return HttpResponse("Success")
    else:
        return HttpResponse("Username and Password do not match")
