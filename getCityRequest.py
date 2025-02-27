import json
import requests
import os
from dotenv import load_dotenv


# Load environment variables from the .env file
load_dotenv()

def hit_weather_service_api(city):
    api_key = os.getenv("API_KEY")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    try: 
        res = requests.api.get(url)
        return res.json()
    except requests.exceptions.RequestException as e:  # Catch any exceptions related to the request
        print(f"Error: {e}")


'''Create a function that will take in the res.json() object and convert it to a dictionary, 
then filter out useless info from the dictionary, convert it back to json and return that.'''

def transform_data(weather_data):
    '''Grab the name, country, temp in F, text which is the sunny, cloudy. Create new dict and add those 4 and return it.'''
    new_dict = {}

    if weather_data:
        city_name = weather_data['location']['name']
        country = weather_data['location']['country']
        temp_f = weather_data['current']['temp_f']
        description = weather_data['current']['condition']['text']

        new_dict["city_name"] = city_name
        new_dict["country"] = country
        new_dict["temp_f"] = temp_f
        new_dict["description"] = description

    return new_dict





if __name__ == '__main__':
    city = input("Please give me a city: ")
    json_weather_obj = hit_weather_service_api(city)
    print(transform_data(json_weather_obj))