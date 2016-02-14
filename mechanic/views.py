from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def add_mechanic(request):
    return render(request, 'mechanic/addmechanic.html')
