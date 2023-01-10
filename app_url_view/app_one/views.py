from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# function based view
def welcome(request):
    return HttpResponse("Welcome to app one")

