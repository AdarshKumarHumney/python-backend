number = 10
print(f"--- Let the countdown begin---")
for i in range(number,0,-1):
    print(f"{i}")
    if(i==3):
        print(f"At {i} ->Ignition start")
    if(i==1):
        print(f"At {i} ->Liftoff")    

