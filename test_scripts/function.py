def calculate_profit(expense_list, earnings):
    total =0
    for i in expense_list:
        total = total+i['Cost']
    net_profit = earnings-total
    return net_profit    
weekly_data = [
    {
        "day": "Monday", 
        "earnings": 900, 
        "expenses": [{'Item':'Fuel', 'Cost':300}]
    },
    {
        "day": "Tuesday", 
        "earnings": 1000, 
        "expenses": [{'Item':'Fuel', 'Cost':300}, {'Item':'Lunch', 'Cost':150}]
    },
    {
        "day": "Wednesday", 
        "earnings": 1100, 
        "expenses": [{'Item':'Fuel', 'Cost':300}, {'Item':'Repair', 'Cost':200}]
    }
]
for i in weekly_data:
    print(f"for {i['day']}")
    net_profit = calculate_profit(i['expenses'],i['earnings'])
    print(f"net profit for {i['day']} is {net_profit}")
