import requests

class ApiError(Exception):
    def __init__(self, message):
        self.message = message


def metal_prices(request):
    base_currency = 'GBP'
    symbol = 'XAU,XAG,XPT,EUR'
    names = {'XAU' : 'Gold',
             'XAG' : 'Silver',
             'XPT' : 'Platinum' }
    
    access_key = 'fdbddc254601e7b9b4e7b65a81bbd5d1'

    resp = requests.get(
        'https://api.metalpriceapi.com/v1/latest'+'?api_key='+access_key+'&base='+base_currency+'&currencies='+symbol)
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET // {}'.format(resp.status_code))

    data = resp.json()
    rates = data['rates']
    rates = rename(rates, names)  
    rates_eur = remove_decimal(get_currency(rates.copy(),'EUR'))
    rates_gbp = remove_decimal(rates)
    rates_eur.pop('EUR')
    rates_gbp.pop('EUR')

    return {'GBP': rates_gbp, 'EUR': rates_eur,}

def get_currency(rates, base_currency):
    base_rate = rates[base_currency]   
    for r in rates.keys():
        rates[r] = rates[r]/base_rate
    
    return rates

def remove_decimal(rates):
    for s in rates.keys():
        rates[s] = float('%.2f'%(1/rates[s]))
    return rates

def rename(rates, names):
    for key in names:
        rates[names[key]] = rates.pop(key)
    return rates
