import requests
import json

def fetch_weather_data(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": location,
        "units": "metric",
        "appid": api_key
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None

def display_weather(weather_data):
    if weather_data is not None:
        city = weather_data['name']
        temperature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description'].capitalize()

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description}")
    else:
        print("No weather data found.")

if __name__ == "__main__":
    api_key = "f5a13ccc86a0cbdcbd8be608f4589fb7"  # Replace with your actual API key from OpenWeatherMap
    location = input("Enter city name or ZIP code: ")
    
    weather_data = fetch_weather_data(api_key, location)
    display_weather(weather_data)
