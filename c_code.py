# Import Packages
import urllib.request
import json


def iss_c_code(lat, lon):
    # This function gets the country code from mapquestapi.com
    key = "8WFGRO07s5wlbkrqo8whKy7vFHNKi1gE"
    url = f"http://www.mapquestapi.com/geocoding/v1/reverse?key={key}&location={lat},{lon}&includeRoadMetadata=true&includeNearestIntersection=true"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    code = result["results"][0]['locations'][0]["adminArea1"]

    return code
