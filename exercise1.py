def check_reorder(inventory_list):
    new_list = []
    for i in inventory_list:
        if i['stock']==0:
            new_list.append(i['product'])
    return new_list
warehouse_stock = [
    {'product': 'Laptop', 'stock': 15},
    {'product': 'Mouse', 'stock': 0},
    {'product': 'Keyboard', 'stock': 2},
    {'product': 'Monitor', 'stock': 0}
]
buy = check_reorder(warehouse_stock)
print(f"the items to buy are{buy}")