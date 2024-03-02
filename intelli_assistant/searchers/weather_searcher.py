import requests
import os

def get_coordinates(api_key, city):
    geocoder_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        'q': city,
        'limit': 1,
        'appid': api_key,
    }

    try:
        response = requests.get(geocoder_url, params=params)
        data = response.json()
        if response.status_code == 200 and data:
            latitude = data[0]['lat']
            longitude = data[0]['lon']
            return latitude, longitude
        else:
            return None, None
    except Exception as e:
        return None, None

def get_weather_by_coordinates(api_key, latitude, longitude):
    weather_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'lat': latitude,
        'lon': longitude,
        'units': 'metric',
        'appid': api_key,
    }

    try:
        response = requests.get(weather_url, params=params)
        data = response.json()
        if response.status_code == 200:
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            return f"Current weather: Temperature {temperature} °C, {description}"
        else:
            return "Sorry, unable to fetch weather information."
    except Exception as e:
        return "Sorry, unable to fetch weather information."

def handle_search_weather(**kwargs):
    city = kwargs.get('city')
    assert city is not None, "city is required."
    api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    assert api_key is not None, "OPENWEATHERMAP_API_KEY is required."
    latitude, longitude = get_coordinates(api_key, city)

    if latitude is not None and longitude is not None:
        return get_weather_by_coordinates(api_key, latitude, longitude)
    else:
        return "Sorry, unable to get city coordinates when fetch weather information."
    