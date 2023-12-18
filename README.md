**GitHub Repository Introduction: SpaceTracker**

Welcome to the SpaceTracker GitHub repository, a Python-powered Flask website that offers a captivating journey into the International Space Station's (ISS) current location and its surroundings. The project adheres to high standards:

1. **Flask Website:** The project leverages Flask to create a dynamic website. It utilizes a template and abstains from user input, offering a hassle-free experience.

2. **API Integration:**
   - Unique API keys are implemented for services such as the Weather Map API and Map Quest API, ensuring secure and personalized data retrieval.
   - The ISS location (latitude and longitude) is dynamically obtained from the [Open Notify API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/), with a captivating ISS image serving as the background.

3. **Weather Information:**
   - Real-time weather information below the ISS is displayed in Celsius, sourced from the [OpenWeatherMap API](https://openweathermap.org/api).

4. **Geolocation:**
   - The Mapquest reverse geolocation API is employed to identify the country beneath the ISS. If over water, it signifies the ISS is over the ocean; otherwise, it reveals the country name.

5. **Country Insights:**
   - If the ISS is above a country, the project fetches additional information about the country and displays its national flag as an image, using the [Restcountries API](https://restcountries.com/#api-endpoints-v3-all).

6. **Distance Calculation:**
   - The distance between Sudbury (the project creator's location) and the ISS is showcased, with a clear indication of the creator's location within the Python code comments.

7. **Data Refresh:**
   - The webpage dynamically refreshes its data with each reload, ensuring up-to-date information on the ISS location and related details.

Explore, fork, and contribute to SpaceTracker as we journey through the cosmos with the International Space Station! 🚀✨
