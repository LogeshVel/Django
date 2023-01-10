from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# function based view
def welcome(request):
    return HttpResponse("Welcome to app one")

# dynamic views
def get_view(request, key, value): # this key, value paramter will be passed from the path variables (specified in the urls.py)
    return HttpResponse(f"Key is {key}\nValue is {value}")

