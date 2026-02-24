import os
import json
script_location = os.path.dirname(__file__)
file_path = os.path.join(script_location,"stock.json")
print(f"I am going to save file here {file_path}")
inventory = {
    'soda':{'price':20,'stock':5},
    'chips':{'price':10,'stock':3},
    'cookie':{'price':5,'stock':10}
}
with open(file_path,"w") as f:
    json.dump(inventory,f)
print("Success the memory file has been created")
with open(file_path,"r") as g:
    saved_data = json.load(g)
print(f"The file contains {saved_data}")        