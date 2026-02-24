import requests
import os
file_location = os.path.dirname(__file__)
script_location = os.path.join(file_location,"img_stars.jpg")
url = "https://api.nasa.gov/planetary/apod"
key_value = {"api_key":"DEMO_KEY"}
response = requests.get(url,params=key_value)
print(response)
if response.status_code == 200:
    value_response = response.json()
    img_url = value_response['url']
    img_response = requests.get(img_url)
    with open(script_location,"wb") as f:
        f.write(img_response.content)
    print("Image savedsuccessfully")
else:
    print("Error detected")    