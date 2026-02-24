daily_earnings=[800,900,700,1200,800]
total_cash=0
print("---Weekly Breakdown")
for day_pay in daily_earnings:
    print(f"processing day: Rs.{day_pay}")
    if(day_pay>=750):
        total_cash=total_cash+day_pay
    else:
        print("skipping bad day")
print("--------------")
print(f"total earnings= {total_cash}")    