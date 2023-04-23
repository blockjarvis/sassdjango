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
    base_currency = 'GBP'
    symbol = 'XAU,XAG,XPT,EUR'
    access_key = '1350778cbe17f00dcddec0f352adadf0'

    resp = requests.get(
        'https://api.metalpriceapi.com/v1/latest'+'?api_key='+access_key+'&base='+base_currency+'&currencies='+symbol)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET // {}'.format(resp.status_code))

    data = resp.json()
    rates = data['rates']    
    rates_eur = remove_decimal(get_currency(rates.copy(),'EUR'))
    rates_gbp = remove_decimal(rates)

    return render(request, 'home/metal_api.html', {'GBP': rates_gbp, 'EUR': rates_eur,})

def get_currency(rates, base_currency):
    base_rate = rates[base_currency]   
    for r in rates.keys():
        rates[r] = rates[r]/base_rate
    
    return rates

def remove_decimal(rates):
    for s in rates.keys():
        rates[s] = float('%.2f'%(1/rates[s]))
    return rates