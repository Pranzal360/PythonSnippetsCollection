# signup weatherapi.com aile alxi lagyo

import requests,json
import os
city = input("Enter the name of the city\n")

url = f""

r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)

temp = wdic["current"]["temp_C"]

os.system(f"say the current weather is {city} is {temp}")