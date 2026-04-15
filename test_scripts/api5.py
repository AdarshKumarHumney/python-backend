import requests
url = "https://jsonplaceholder.typicode.com/todos"
my_data = {'userId':1,
           'title':"Mastering Python requests",
           'completed':False}
try:
    response = requests.post(url,json = my_data)
    if response.status_code == 201:
        print("Success")
        print(response.json())
    else:
        print("Somehting went wrong")    
except Exception as e:
    print(f"The error is {e}")        