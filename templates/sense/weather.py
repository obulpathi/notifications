import requests
import json

def sense():
    result = requests.get("http://api.wunderground.com/api/{{apikey}}/conditions/q/{{state}}/{{city}}.json")
    weather = result.json()
    if weather['current_observation']['feelslike_f'] > {{threshold}}:
        return True, "The temperature is above {{threshold}} degrees today!"

    return False, ""

