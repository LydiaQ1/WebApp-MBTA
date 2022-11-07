import urllib.request
import json
from pprint import pprint

MAPQUEST_API_KEY = 'kL5zMDyP7plpwJ8NyY45E9E832gjA6XV'

url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
f = urllib.request.urlopen(url)
response_text = f.read().decode('utf-8')
response_data = json.loads(response_text)
pprint(response_data)


