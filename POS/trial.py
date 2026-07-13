list1 = ['message','name','id']
tup2 = [("hello","mma",1),("hello1","wwe",2)]
dict_list = []
for i in tup2:
    dict_list.append(dict(zip(list1,i)))
for i in dict_list:
    print(i['message'])

    response = self.im.printList()
        if not response['value']:
            print("There is a problem with the database")
            return True
        elif not response['data']:
            print("There are not items now to update")
            return True
        else:
            while True:
                while True:
                    try:
                        id = int(input("Select the id you want to update"))
                        break
                    except ValueError:
                        print("Please select the id in integer")
                response_main = self.im.searchById(id)
                if not response_main['value']:
                    print("Id cannot be searched due to problem in database")
                    return True
                elif not response_main['data']:
                    print(f"There are no data with the id - {id} please select another id")
                    continue
                else:
                    print(response_main['data'])
                    choice = input("Select from the choice - NAME || STOCK || PRICE || EXIT to make an update").strip().lower()
                    if choice == "name":
                        new_name = input("Please select the new name of the product")
                        response = self.im.updateName(id,new_name)
                        if response['value']:
                            print("The name is updated successfully")
                            break
                        else:
                            print("There was a problem in updating the name")
                    elif choice == "price":
                        while True:
                            try:
                                new_price = float(input("Please input the new price of the stock"))
                                break
                            except ValueError:
                                print("Please enter the price in numericals")
                        response = self.im.updatePrice(id,new_price)
                        if response['value']:
                            print("The price was updated successfully")
                            break
                        else:
                            print("There was a problem in updating the price")
                    elif choice == "stock":
                        while True:
                            try:
                                new_stock = int(input("Input the new stock value"))
                                break
                            except ValueError:
                                print("Please input the value in digits") 
                        print(f"The current stock is - {response_main['data']['item_quant']}")
                        update_stock = response_main['data']['item_quant']+new_stock
                        response = self.im.updateStock(id,update_stock)
                        if response['value']:
                            print(f"The stock is updated. New stock is -{update_stock} ")
                            break
                        else:
                            print("Ther was a problem in updating the stock")
                    elif choice == "exit":
                        print("Exiting the update function")
                        break
                    else:
                        print("Please select from the above list of choices")
                    continue
        return True
