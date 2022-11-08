import urllib.request
import json
from pprint import pprint

MAPQUEST_API_KEY = 'kL5zMDyP7plpwJ8NyY45E9E832gjA6XV'

url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
# pprint(response_data)

def latlng():
    d = dict()
    d = response_data
    lat = d['results'][0]['locations'][0]['latLng']['lat']
    lng = d['results'][0]['locations'][0]['latLng']['lng']
    return (lat,lng)

# print(latlng())

def geturl(place=None):
    if place:
        place = place.replace(" ","%20")
        return f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place}'

# print(geturl('Wellesley College'))

def getstop(lat,lng):
    YOUR_MBTA_API_KEY = 'e4b760e47fa14ad0b8f8cbd927c92ec9'
    url = f'https://api-v3.mbta.com/stops?api_key={YOUR_MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={lng}'
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    d = dict()
    d = response_data
    stop = d['data'][0]['attributes']['name']
    wheelchair = d['data'][0]['attributes']['wheelchair_boarding']
    if wheelchair == 0:
        wheelchairok = 'is no information of'
    if wheelchair == 1:
        wheelchairok = "is"
    else:
        wheelchairok = "is no"
    return f'The nearest MBTA stop is {stop}. There {wheelchairok} wheelchair accessible for this stop'

print(getstop(42.36553,-71.0612))

