# Import Packages
import urllib.request
import json

def iss_weather(lat, lon):
	# This function returns temperature, google map link, weather description and country name
	key = '778fedad8e7d9547b3eae10f40c89437'
	url= f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}' #This API returns weather and country code of provided location
	response = urllib.request.urlopen(url)
	result = json.loads(response.read())
	temp = round(result['main']['temp'] - 273.15, 2) #Temprature of space station's current location in Celsius
	desc = result["weather"][0]['description']
	link = f'https://www.google.com/maps/place/{lat}+{lon}'

	if 'country' in result['sys']:
		code = result['sys']['country'].lower()
		url3 = f'https://restcountries.com/v2/alpha/{code}' #This API returns country name for this code
		response3 = urllib.request.urlopen(url3)
		result3 = json.loads(response3.read())
	else:
		code = ''
	
	#Checks code and returns country name if space station is over a country else returns ocean
	if len(code) != 0:
		country = result3['name']
	else:
		country = 'ocean'
		
	return temp, link, desc, country