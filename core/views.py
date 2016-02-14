from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'core/login.html')


@login_required(login_url='/')
def home(request):
    return render(request, 'core/context.html')


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
