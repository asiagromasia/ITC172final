from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    # index is different than the rest so now you have to do the name of the view
    #path('techtypes/', views.techtypes, name='techtypes'),
]