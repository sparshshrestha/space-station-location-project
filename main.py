# Importing all the packages and python files
from flask import Flask, render_template
from space import iss_loc
from weather import iss_weather
from flag import flag
from distance import dist
from c_code import iss_c_code
import random

# Creating an app
app = Flask('app')


# Routing the app to main page
@app.route('/')
def index():
    """ This function renders the index.html page """
    lat, lon = iss_loc()  # Get latitude and longitude of the ISS
    c_code = iss_c_code(lat, lon)  # Get country code from the lat and lon
    print("======================================")
    print(c_code)
    temp, link, desc, country = iss_weather(
        lat, lon
    )  # Get the temperature, google map link, weather description and country name
    if c_code == '':  # If the ISS is over the ocean
        c_code = 'XZ'
        flag_img = 'static/images/ocean.jpg'  # Image of the ocean
        result = ''  # Pass an empty result
    else:
        flag_img, result = flag(c_code)  # Get flage image link and the result
    distance = round(dist(lat, lon, 46.5247397, -80.928819),
                     2)  # Get distance from ISS
    # 46.5247397, -80.928819 is my coordinates
    # Since the assignment required not to get user input, I can't get location of the user, so i used my location
    return render_template("index.html",
                           lat=lat,
                           lon=lon,
                           c_code=c_code,
                           temp=temp,
                           link=link,
                           desc=desc,
                           flag_img=flag_img,
                           distance=distance,
                           country=country,
                           result=result)


# Runs the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=random.randint(2000, 9000))
