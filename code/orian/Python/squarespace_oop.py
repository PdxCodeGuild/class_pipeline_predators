import requests
import json

class Squarespace:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Authorization': self.api_key,
            'User-Agent': 'Alex-postman'
        }
    def get_orders(self):
      
        response = requests.get(self.base_url+'commerce/orders', headers= self.headers)
        print(response.json())

    def get_profiles(self):
       
        response = requests.get(self.base_url+'profiles/', headers= self.headers)
        print(response.json())


space = Squarespace("Bearer b6237cac-d973-4b66-8b50-3bf492c4b3c1","https://api.squarespace.com/1.0/")
space.get_profiles()