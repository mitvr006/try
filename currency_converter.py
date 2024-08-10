import requests
import json

user_key = "009751434dd24478d8ddf28f"
url = f"https://v6.exchangerate-api.com/v6/{user_key}/latest/USD"
response = requests.get(url,timeout=10)
# print(response.json())

currency_data =response.json()

