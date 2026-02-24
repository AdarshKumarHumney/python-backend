import random
import time
options = ['heads','tails']
flip = random.choice(options)
print("flipping the coin")
time.sleep(2)
print(f"you got {flip}")