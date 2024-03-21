# WeatherApp

This Python script fetches weather information based on user-provided location using the OpenWeatherMap API.



## Setup

1. Clone the repository or download the script.
2. Obtain an API key from OpenWeatherMap by signing up at https://home.openweathermap.org/users/sign_up.
3. Replace `'YOUR_API_KEY'` in the script with your actual API key.

## Usage

1. Run the script using Python: `python weather_app.py`.
2. Enter the location when prompted.
3. The script will then fetch and display the current weather information for the provided location.

## Functionality

- The script prompts the user to input a location.
- It then fetches the latitude and longitude coordinates corresponding to the provided location.
- With the coordinates, it retrieves weather information from the OpenWeatherMap API.
- The weather information fetched includes a brief description of the current weather conditions.

## Error Handling

- If the location provided by the user is invalid, the script will raise a ValueError.
- If there's an error fetching data from the API, it will print an appropriate error message.


