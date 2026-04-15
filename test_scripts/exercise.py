def calculate_final_bill(cart_items):
    total = 0
    for i in cart_items:
        total+= i['price']
    if total>500:
        final_pay = total-(total*5/100)
        return final_pay    
    else:
        return total    
cart = [
    {'name': 'Headphones', 'price': 400},
    {'name': 'Phone Case', 'price': 150},
    {'name': 'Screen Guard', 'price': 100}
]
pay = calculate_final_bill(cart)
print(f"the final amount to pay is {pay}")    