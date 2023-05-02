from django.contrib import admin
from django.urls import path
from .views import ptindex
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pt', views.ptindex, name='pthome'),
]
