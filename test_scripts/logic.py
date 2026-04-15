target_profit=20000
net_profit=18250
if net_profit>=target_profit:
    print("great month")
    print("Time to celebrate")
elif 15000<=net_profit<20000:
    print("decent month keep pushing")
else:
    print("Missed Target")
    diff=target_profit-net_profit
    print(f"You neeed {diff} more to hit the goal")
print("End of report")    