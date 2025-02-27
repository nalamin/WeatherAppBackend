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
        # print(res.json())
        return res.json()
    except requests.exceptions.RequestException as e:  # Catch any exceptions related to the request
        print(f"Error: {e}")



'''Create a function that will take in the res.json() object and convert it to a dictionary, 
then filter out useless info from the dictionary, convert it back to json and return that.'''


if __name__ == '__main__':
    city = input("Please give me a city: ")
    hit_weather_service_api(city)