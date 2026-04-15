api_response = {
    "status": "success",
    "data": [
        {
            "id": "bitcoin",
            "current_price": {
                "usd": 96000,
                "inr": 8000000
            },
            "tags": ["crypto", "gold", "payment"]
        },
        {
            "id": "ethereum",
            "current_price": {
                "usd": 2500,
                "inr": 200000
            },
            "tags": ["smart-contract", "defi"]
        }
    ]
}
print("Price of bitcoin in usd")
price_of_bitcoin=api_response["data"][0]['current_price']['usd']
print(price_of_bitcoin)
print("The name of second coin in the list")
name_of_second_coin= api_response["data"][1]['id']
print(name_of_second_coin)
print("The first tag of ethereum coin")
first_tag = api_response["data"][1]['tags'][0]
print(first_tag)

print("--------------------------------------------------------------------------------")
portfolio = {
    "owner": "Adarsh",
    "assets": []  # This list is currently empty!
}
new_coin={"name": "Solana", "price": 140, "amount": 10}
portfolio["assets"].append(new_coin)
new_coin2={"name": "Bitcoin", "price": 96000, "amount": 0.5}
portfolio["assets"].append(new_coin2)
for details in portfolio["assets"]:
    print(f"I own {details['amount']} of {details['name']}")
    total= details['price']*details['amount']
    print(f"Total worth is {total}")