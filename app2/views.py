from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kohli(requst):
    return HttpResponse('kohli is a world best batsman')