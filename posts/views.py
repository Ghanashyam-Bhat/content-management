from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/auth/")
def posts(request):
    return HttpResponse("Welcome")
