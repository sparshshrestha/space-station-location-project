# Import Packages
import urllib.request
import json


def flag(name):
    try:
        # This function returns the flag link for a country and its json data
        url = f'https://restcountries.com/v3.1/alpha/{name}'
        print(f"Requesting URL: {url}")
        response = urllib.request.urlopen(url)
        content = response.read()
        print(f"Response Content: {content}")
        result = json.loads(content)
        flag = result[0]["flags"]['png']
        return flag, result
    except Exception as e:
        return None, f"Error: {e}"
