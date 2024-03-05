import requests

def get_weather_forecast(city, api_key):
    """
    Get the weather forecast for a given city using the OpenWeatherMap API.

    Parameters:
    city (str): The name of the city to get the weather forecast for.
    api_key (str): The API key for the OpenWeatherMap API.

    Returns:
    dict: A dictionary containing the weather forecast data.
    """
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric' # Use metric units (Celsius)
    }
    response = requests.get(base_url, params=params)
    return response.json()