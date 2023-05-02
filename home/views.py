from django.shortcuts import render
from django.http import JsonResponse
import requests


# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def ptindex(request):
    """ A view to return the index page """

    return render(request, 'home/ptindex.html')
