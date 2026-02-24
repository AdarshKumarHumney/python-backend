import requests
url = "https://jsonplaceholder.typicode.com/posts"
my_params = {'userId':5}
print(f"Searching with params: {my_params}")
try:
    response = requests.get(url,my_params)
    if response.status_code==200:
        data = response.json()
        print(f"Found {len(data)} data by user")
        if len(data)>0:
            found_title = data.get('title',"NO title was found")
            print(f"{found_title}")
    else:
        print("Failed")
except Exception as e:
    print(f"Error is {e}")          
              