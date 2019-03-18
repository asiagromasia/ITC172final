from django.test import TestCase
from .models import ProductTypes, Products, Orders, Reviews
from django.urls import reverse

# Create your tests here.
class ProductTypesTest(TestCase):
    def test_stringOutput(self):
        producttype = ProductTypes(typename = 'Test Product Type')
        self.assertEqual(str(producttype), producttype.typename)
    def test_tablename(self):
        self.assertEqual(str(ProductTypes._meta.db_table), 'producttypes')
        
class ProductTest(TestCase):
    def test_stringOutput(self):
        product = Products(productname = 'Test Product Title')
        self.assertEqual(str(product), product.productname)
    def test_tablename(self):
        self.assertEqual(str(Products._meta.db_table), 'products')

class OrderTest(TestCase):
    def test_stringOutput(self):
        order = Orders(id = '1')
        self.assertEqual(str(order), order.id)
    def test_tablename(self):
        self.assertEqual(str(Orders._meta.db_table), 'orders')
        
class ReviewTest(TestCase):
    def test_stringOutput(self):
        review = Reviews(id = '1')
        self.assertEqual(str(review), review.id)
    def test_tablename(self):
        self.assertEqual(str(Reviews._meta.db_table), 'reviews')
        
 #Testing a view

class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'storeapp/index.html')
        
class TestProductTypes(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getproducttypes'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('getproducttypes'))
        self.assertTemplateUsed(response, 'storeapp/producttypes.html')
        
#Login identification would be required to pass these tests.
class TestNewOrder(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('neworder'))
        self.assertEqual(response.status_code, 200)
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('neworder'))
        self.assertTemplateUsed(response, 'storeapp/neworder.html')