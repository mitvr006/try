import requests
import json
import logging
logging.basicConfig(level=logging.INFO)

def temp():
    logging.debug("temp function start")
    location_name = str(input("Enter the location:"))
    user_key = "73b8d31d7b484d4f8d1145934242907"
    url = f"http://api.weatherapi.com/v1/current.json?key={user_key}&q={location_name}&aqi=yes"
    response = requests.get(url,timeout=10)
    # print(response)

    weather_data=response.json()
    
    loc=weather_data["location"]["name"]
    temp=weather_data["current"]["temp_c"]

    logging.info(f"temp in {loc} is {temp} celsius")
    logging.debug("find_temp function end")

temp()




