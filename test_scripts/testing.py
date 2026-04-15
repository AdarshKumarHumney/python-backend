import requests
import time
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)
getdata = response
print(f"{response}")