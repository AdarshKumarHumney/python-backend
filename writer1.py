import os

# 1. Get the folder where THIS script lives
# __file__ is a special variable that holds the script's own address
script_location = os.path.dirname(__file__)

# 2. Combine that location with your new filename
# This creates a full path like: C:/Users/Adarsh/MyFolder/memory.txt
file_path = os.path.join(script_location, "memory.txt")

# 3. Use that FULL path
with open(file_path, "w") as f:
    f.write("I am exactly where the script is!")

print(f"Saved to: {file_path}")