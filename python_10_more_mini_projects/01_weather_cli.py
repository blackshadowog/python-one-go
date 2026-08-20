import urllib.request, json
city = input("Enter city: ")
try:
    data = json.load(urllib.request.urlopen(f"https://wttr.in/{city}?format=j1"))
    c = data["current_condition"][0]
    print("Temperature:", c["temp_C"], "C")
    print("Humidity:", c["humidity"], "%")
    print("Condition:", c["weatherDesc"][0]["value"])
except Exception:
    print("Could not fetch weather data.")
