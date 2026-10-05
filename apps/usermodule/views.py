from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello from User Module!")
# Create your views here.
