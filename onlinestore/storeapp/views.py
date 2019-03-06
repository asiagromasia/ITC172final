from django.shortcuts import render, get_object_or_404
from .models import ProductTypes, Products, Orders, Reviews
from .forms import ProductsForm

# Create your views here.
def index (request):
    return render(request, 'storeapp/index.html')

def getproducts
    products_list = Products.objects.all()
    return render(request, 'storeapp,products.html', {'products_list': products_list})

def productsdetails
    detail=get_object_or_404(Products, pk=id)
    return render(request, 'storeapp/productdetails.html',{'detail' : detail})

def getreviews
    reviews_list = Reviews.objects.all()
    return render(request, 'storeapp,reviews.html', {'reviews_list': reviews_list})

def reviewdetails
    detail=get_object_or_404(Reviews, pk=id)
    return render(request, 'storeapp/reviewdetails.html',{'detail' : detail})
