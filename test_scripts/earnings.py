daily_earnings=800
days_worked=25
fuel_cost=3000
daily_tip=50
total_revenue=(daily_earnings+daily_tip)*days_worked
net_revenue=total_revenue-fuel_cost
print("-----Monthly Report-----")
print(f"Total Revenue={total_revenue}")
print(f"Fuel Cost={fuel_cost}")
print(f"Net profit={net_revenue}")