from django.contrib import admin
from django.urls import path
from .views import metal_api
from . import views

urlpatterns = [
    path('metal', views.metal_api, name='metal_api'),
    path('', views.index, name='home')
]
