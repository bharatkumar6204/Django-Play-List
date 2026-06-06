from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Shop home Page')

def about(request):
    return HttpResponse('Shop about page')