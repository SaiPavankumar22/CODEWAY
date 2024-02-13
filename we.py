import requests as rq

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("WELCOME TO THE WEATHER FORCAST")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
key = '30d4741c779ba94c470ca1f63045390a'


city = input("Please enter the city name!! \n")

weather_data = rq.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={key}")

print("\n\n")

if weather_data.status_code==404:

    print(f"Sorry!! City -{city} not found.")
   
else:

    weather = weather_data.json()["weather"][0]["main"]

    temperature_farenheat= round(weather_data.json()["main"]["temp"])

    temperature_celsius=round((temperature_farenheat-32)*(5/9))
    sunrise = weather_data.json()["sys"]["sunrise"]

    sunset = weather_data.json()["sys"]["sunset"]

    print(f"Weather at {city} is : {weather}\n")

    print(f"Temperature in {city} is : {temperature_celsius}°c\n")

    print(f"Sunrise : {sunrise}\n")

    print(f"Sunset : {sunset}\n")