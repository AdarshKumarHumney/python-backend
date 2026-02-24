my_profile = {
    "name": "Adarsh",
    "role": "Python Student",
    "Level": 1
}
print(f"User {my_profile['name']} is currently level {my_profile['Level']}")
my_profile["Level"]=2
my_profile["next_goal"]="Loops Master"
print(f"{my_profile}")