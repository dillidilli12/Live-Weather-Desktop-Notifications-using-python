import requests
from pprint import pprint
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
n = ToastNotifier()

API_KEY = '431cfbbd8bce4a578ba9da8c213dcf77'

City = input("Enter the city name : ")
base_url = "https://api.openweathermap.org/data/2.5/weather?q=" + City + "&appid=" + API_KEY

weather_data = requests.get(base_url).json()

current_temp = weather_data["main"]["temp"] - 273.15 # Convert Kelvin to Celsius
current_temp_feels_like = weather_data["main"]["feels_like"] - 273.15
max_temp = weather_data["main"]['temp_max'] - 273.15
min_temp = weather_data["main"]["temp_min"] - 273.15

result = f"Current Temperature: {current_temp:.1f}°C\nFeels like: {current_temp_feels_like:.1f}°C\nMax Temperature: {max_temp:.1f}°C\nMin Temperature: {min_temp:.1f}°C"

n.show_toast("Weather update for " + City, result, duration=10)
