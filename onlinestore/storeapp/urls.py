from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    # index is different than the rest so now you have to do the name of the view
    path('neworder/', views.neworder, name='neworder'),
    path('getproducts/<int:id>', views.getproducts, name='getproducts'),
    path('getreviews/<int:id>', views.getreviews, name='getreviews'),
    path('productdetails/<int:id>', views.productdetails, name='productdetails'),
    path('reviewdetails/<int:id>', views.reviewdetails, name='reviewdetails'),
    path('getproducttypes/', views.getproducttypes, name='getproducttypes'),
]