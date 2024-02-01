import requests
import json
import pyttsx3

city = input("Enter Your City Name: ")
url = f"http://api.weatherapi.com/v1/current.json?key=25e85d1e12264bf58fd162106243001&q={city}&aqi=no"

r = requests.get(url)
# print(r.text)
wdic=json.loads(r.text)
engine=pyttsx3.init();
text=(wdic["current"]["temp_c"])
var=f"The temperature of {city} is"+str(text)+"degree celcius"
engine.say(var)
engine.runAndWait()
