from django.shortcuts import render
from django.http import JsonResponse
import requests

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

class ApiError(Exception):
    def __init__(self, message):
        self.message = message


def metal_api(request):
    base_currency = 'USD'
    symbol = 'XAU' 
    endpoint = 'latest'
    access_key = 'od07ua0018t61i6450d7kgch0bz2b2nxlmw4cat353v0p6orjm1bq366zfe2'

    resp = requests.get(
        'https://metals-api.com/api/'+endpoint+'?access_key='+access_key+'&base='+base_currency+'&symbols='+symbol)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /'+endpoint+'/ {}'.format(resp.status_code))

    data = resp.json()
    return JsonResponse(data)
