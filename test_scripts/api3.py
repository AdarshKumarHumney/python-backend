import requests
url = "https://jsonplaceholder.typicode.com/users"
try:
    response = requests.get(url)
    if response.status_code ==200:
        get_response = response.json()
        for find in get_response:
            if find['id']==5:
                id_name = find['name']
                address = find['address']['city']
                print(f"{id_name} lives in {address}")
    else:
        print("There was some error")            
except Exception as e:
    print(f"Error is {e}")