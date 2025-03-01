import urllib.request
import json

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = 'kL5zMDyP7plpwJ8NyY45E9E832gjA6XV'
MBTA_API_KEY = 'e4b760e47fa14ad0b8f8cbd927c92ec9'


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it


def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.

    Both get_lat_long() and get_nearest_station() might need to use this function.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data
    

def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding API URL formatting requirements.
    """
    d = dict()
    place_name = place_name.replace(" ","%20")
    place_name =place_name + ',Boston,MA'
    url = MAPQUEST_BASE_URL + f'?key={MAPQUEST_API_KEY}&location={place_name}'
    # print(url)
    d = get_json(url)
    lat = d['results'][0]['locations'][0]['latLng']['lat']
    lng = d['results'][0]['locations'][0]['latLng']['lng']
    return (lat,lng)



def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    url = MBTA_BASE_URL + f'?api_key={MBTA_API_KEY}&sort=distance&filter%5Blatitude%5D={latitude}&filter%5Blongitude%5D={longitude}'
    d = get_json(url)
    stop = d['data'][0]['attributes']['name']
    wheelchair = d['data'][0]['attributes']['wheelchair_boarding']
    return (stop,wheelchair)


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    lat,lng = get_lat_long(place_name)
    stop,wheelchair = get_nearest_station(lat,lng)
    if wheelchair == 0:
        wheelchairok = 'NA'
    if wheelchair == 1:
        wheelchairok = "Yes"
    else:
        wheelchairok = "No"
    return (stop,wheelchairok)


def main():
    """
    You can test all the functions here
    """
    place_name = 'Boston Common'
    # print(get_lat_long(place_name))
    print(find_stop_near(place_name))


if __name__ == '__main__':
    main()
