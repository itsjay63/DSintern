
city = input("Enter the city name: ")

api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=e9185b28e9969fb7a300801eb026de9c"

import requests

response = requests.get(api)

jsondata = response.json()

jsondata['main']['temp']