import requests
import json

print("weather app")
result = False
while not result:
    answer = input("enter a valid city ")
    r = requests.get('https://geocoding-api.open-meteo.com/v1/search', params={"name": answer, "count": 1})
    data = r.json()  

    
    if "results" in data and len(data["results"]) > 0:
        result = True
    else:
        print("City not found. Please try again.")

latitude = data["results"][0]["latitude"]
longitude = data["results"][0]["longitude"]


m = requests.get('https://api.open-meteo.com/v1/forecast', params={"latitude": latitude, "longitude": longitude , "current" : "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code"})
weather_data = m.json()  
weather_code = {
    0: "clear sky",
    1: "mainly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "fog",
    48: "depositing rime fog",
    51: "light drizzle",
    53: "moderate drizzle",
    55: "dense drizzle",
    56: "light freezing drizzle",
    57: "dense freezing drizzle",
    61: "slight rain",
        63: "moderate rain",
        65: "heavy rain",
        66: "light freezing rain",
        67: "heavy freezing rain",
        71: "slight snowfall",
        73: "moderate snowfall",
        75: "heavy snowfall",
        77: "snow grains",
        80: "slight rain showers",
        81: "moderate rain showers",
        62: "violent rain showers",
        85: "slight snow showers",
        86: "heavy snow showers",
        95: "thunderstorm",
        96: "thunderstorm with slight hail",
        97: "heavy thunderstorm",
        99: "thunderstorm with heavy hail"
}

print("weather in", answer)
print("temp is :", weather_data["current"]["temperature_2m"])
print("humidity is :", weather_data["current"]["relative_humidity_2m"])
print("wind speed is :", weather_data["current"]["wind_speed_10m"])
print("weather code is :", weather_code[weather_data["current"]["weather_code"]])







