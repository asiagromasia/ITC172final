from django import forms
from .models import ProductTypes, Products, Orders, Reviews

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'
