from django import forms
from .models import ProductTypes, Products, Orders, Reviews

class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = '__all__'

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'