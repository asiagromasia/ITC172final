from django.shortcuts import render, get_object_or_404
from .models import ProductTypes, Products, Orders, Reviews
from .forms import OrdersForm, ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index (request):
    return render(request, 'storeapp/index.html')

def getproducts (request, id):
    products_list = Products.objects.filter(producttype=id)
    return render(request, 'storeapp/products.html', {'products_list': products_list})

def productdetails (request, id):
    detail=get_object_or_404(Products, pk=id)
    return render(request, 'storeapp/productdetails.html',{'detail' : detail})

def getreviews (request, id):
    reviews_list = Reviews.objects.filter(reviewproduct=id)
    return render(request, 'storeapp/reviews.html', {'reviews_list': reviews_list})

def reviewdetails (request, id):
    detail=get_object_or_404(Reviews, pk=id)
    return render(request, 'storeapp/reviewdetails.html',{'detail' : detail})

def getproducttypes (request):
    types_list=ProductTypes.objects.all()
    return render(request, 'storeapp/producttypes.html', {'types_list' : types_list})

@login_required
def neworder(request):
    form=OrdersForm
    if request.method=='POST':
        form=OrdersForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=OrdersForm()
            # you could re-direct here once form is submitted instead off  generating new form
    else:
        form=OrdersForm()
    return render(request, 'storeapp/neworder.html', {'form': form})   

@login_required
def newproduct(request):
    form=ProductForm
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            post=form.save(commit=True)
            post.save()
            form=ProductForm()
            # you could re-direct here once form is submitted instead off  generating new form
    else:
        form=ProductForm()
    return render(request, 'storeapp/newproduct.html', {'form': form})  

def loginmessage(request):
    return render(request, 'storeapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'storeapp/logoutmessage.html')    