from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.
from django.http import HttpResponse
def index(request):
    Products = Product.objects.all()
    print(Product)
    n = len(Products)
    nSlides =n//4 + ceil((n/4)-(n//4))
    params = {'no_of slides': nSlides,'range' : range(1,nSlides),'product': Products}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def search(request):
    return HttpResponse("We are at search")

def productview(request):
    return HttpResponse("We are at product")

def checkout(request):
    return HttpResponse("We are at checkout")
