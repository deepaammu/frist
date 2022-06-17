from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(requst):
    return HttpResponse('dhoni is a best captain')