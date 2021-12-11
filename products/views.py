from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index(request):
    response = HttpResponse("Hello World")
    products = Product.objects.all()
    return render(request, "index.html", {"products": products})


def new_products(request):
    return HttpResponse("Welcome to new products")