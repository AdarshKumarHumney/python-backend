def paycheque(employee_list):
    for i in employee_list:
        if i['type'].lower()=='manager':
            pay = 500*i['hours']
        if i['type'].lower()== 'intern':
            pay = 200*i['hours']
        print(f"{i['name']} earns Rs. {pay}")    
employees = [
    {'name': 'Rahul', 'hours': 40, 'type': 'Manager'},
    {'name': 'Adarsh', 'hours': 30, 'type': 'Intern'},
    {'name': 'Priya', 'hours': 40, 'type': 'Intern'}
]
paycheque(employees)