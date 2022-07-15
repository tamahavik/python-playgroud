import requests
import datetime as dt

# URL = "http://api.open-notify.org/iss-now.json"
#
# response = requests.get(url=URL)
# if response != 200:
#     response.raise_for_status()
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

URL = "https://api.sunrise-sunset.org/json"
LAT = 51.1
LNG = -0.2

parameters = {
    "lat": LAT,
    "lng": LNG,
    "formatted": 0
}

response = requests.get(URL, params=parameters)
if response.status_code != 200:
    response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
time_now = dt.datetime.now()

print(sunrise, sunset, time_now)
