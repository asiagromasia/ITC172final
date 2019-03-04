from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductTypes(models.Model):
    typename = models.CharField(max_length = 255)
    typedescription = models.TextField()
    typeuser = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.typename
    class Meta:
        db_table = 'producttypes'

class Products(models.Model):
    productname = models.CharField(max_length = 255)
    producttype = models.ForeignKey(ProductTypes, on_delete = models.DO_NOTHING)
    productprice = models.DecimalField(max_digits = 5, decimal_places = 2)
    productuser = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    productdescription = models.TextField()
    def __str__(self):
        return self.productname
    class Meta:
        db_table = 'products'

class Orders(models.Model):
    orderclient = models.CharField(max_length = 255)
    orderplacedate = models.DateField()
    orderdeliverydate = models.DateField()
    orderproduct = models.ForeignKey(Products, on_delete = models.DO_NOTHING)
    orderaddress = models.CharField(max_length = 255)
    orderinstructions = models.TextField()
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'orders'

class Reviews(models.Model):
    reviewproduct = models.ForeignKey(Products, on_delete = models.DO_NOTHING)
    reviewcomment = models.TextField()
    reviewrating = models.SmallIntegerField()
    reviewdate = models.DateField()
    reviewreply = models.TextField()
    revieworder = models.ForeignKey(Orders, on_delete = models.DO_NOTHING)
    def __str__(self):
        return self.id
    class Meta:
        db_table = 'reviews'