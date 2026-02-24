import os

# 1. Get the current address
current_location = os.getcwd() 

print(f"I am saving files here: {current_location}")

# 2. Let's create the file again just to be sure
with open("memory.txt", "w") as f:
    f.write("Found me!")

print("File created again.")

# 3. Check if Python can see it
if "memory.txt" in os.listdir():
    print("Python says: 'I can see the file!'")
else:
    print("Python says: 'I cannot find it.'")