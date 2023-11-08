import requests     # Python requests is a library for making HTTP requests.
import json
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
city = input("Enter the name of your city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=7f8ab4e088894891922113357232308&q={city}"

r = requests.get(url)
# print(r.content)

wdict = json.loads(r.content)
temp = wdict["current"]["temp_c"]
DateTime = wdict["location"]["localtime"]
condition = wdict["current"]["condition"]["text"]

print(temp)
print(DateTime)
print(condition)

if condition == "Rain":
    speak.Speak(f"Temperature of {city} on {DateTime} is {temp} degree celsius and there is a possibility of {condition}")

else:
    speak.Speak(f"Temperature of {city} on {DateTime} is {temp} degree celsius and weather is {condition}")