# Import Packages
import urllib.request
import json


def iss_loc():
    # This function identifies the latitude nad longitude of the ISS
    url = 'http://api.open-notify.org/iss-now.json'  #This API returns location information of space station in real-time
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    lat = result['iss_position'][
        'latitude']  #Latitude position of space station
    lon = result['iss_position'][
        'longitude']  #Longitude position of space station
    return lat, lon
