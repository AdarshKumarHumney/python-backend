def ConvertToDict(list,table):
    admin_keys=["name","email","password"]
    user_keys = ["name","email","age"]
    result = []
    keys = admin_keys if table.lower()=="admin" else user_keys
    for i in list:
        added = dict(zip(keys,i))
        result.append(added)
    return result
table_choice = input("Please select the table user or admin")
list1 = [("Adarsh","Adarsh@gmail.com","12345"),
         ("Avinabh","Avinabh@gmail.com","12345")]
output_1 = ConvertToDict(list1,table_choice)
print(output_1)