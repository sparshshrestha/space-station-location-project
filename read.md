Requirements:
1. Syntax, spelling, grammar - Code works so no syntax error.
2. All the code is commented.
3. Both .zip format and link to my code in replit.com will be provided
4. Built a Python powered flask website that does not have user input. A template is used.
5. Unique keys for all APIs that require them are used. Weather Map API and Map Quest API require Unique API keys.
6. The location (latitude and longitude) of the ISS is shown and an image of it is used as a backgroung image. Location is extracted from from http://open-notify.org/Open-Notify-API/ISS-Location-Now/
7. On the same page, the weather below the space station is shown in Celsius using https://openweathermap.org/api
8. Displays what country the ISS is above using the Mapquest reverse geolocation API (https://developer.mapquest.com/documentation/geocoding-api/) If the ISS is over the water, it shows that the iss is over the ocean, otherwise, it show the country it is above.
9. If the ISS is above a country, it shows some information about the country and show the national flag as an image using the https://restcountries.com/#api-endpoints-v3-all API
10. The distance between my location (Sudbury) and the ISS is shown, I have commented in the Python code where I am located.\
11. The data refreshs each time the HTML page is reloaded.