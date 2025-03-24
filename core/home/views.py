from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return render(req, 'home/index.html')

def success_page(req):
    return HttpResponse("This is a success page")