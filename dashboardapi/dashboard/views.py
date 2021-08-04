from .models import Products
from django.shortcuts import render
from django.http import JsonResponse
# from dashboard.models import Order
from django.core import serializers


# Create your views here.
def index(request):
    return render(request, 'index.html', {})


def pivot_data(request):
    dataset = Products.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)


def products(request):
    return render(request, 'products.html', {})


def add_product(request):
    return render(request, 'add-product.html', {})


def edit_product(request):
    return render(request, 'edit-product.html', {})


def accounts(request):
    return render(request, 'accounts.html', {})
