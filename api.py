import datetime as dt
import requests
import pandas as pd


base_url = "http://api.openweathermap.org/data/2.5/forecast?"
api_key = "56facac7d7a894254033f3692862b5ca"
city = "Karachi"

url = base_url + "appid=" + api_key + "&q=" + city

response = requests.get(url).json()

date = []
time = []
temprature = []
weather = []
humidity = []
wind_spd = []
clouds = []

for i in response["list"]:
    temprature.append(i["main"]["temp"]-273.15)
    date.append(i["dt_txt"].split()[0])
    time.append(i["dt_txt"].split()[1])
    humidity.append(i["main"]["humidity"])
    weather.append(i["weather"][0]["main"])
    clouds.append(i["clouds"]["all"])
    wind_spd.append(i["wind"]["speed"])

dict = {
    "temprature": temprature,
    "date": date,
    "time": time,
    "humidity": humidity,
    "condition": weather,
    "cloud_coverage": clouds,
    "wind": wind_spd
}
    
df = pd.DataFrame(dict)
df.to_csv("temprature.csv")