users = [
    {"full_name": "Adarsh Singh", "email": "adarsh@example.com"},
    {"full_name": "Elon Musk", "email": "elon@tesla.com"},
    {"full_name": "Sam Altman", "email": "sam@openai.com"}
]
clean_user=[]
for i in users:
    clear_dict={}
    name_split = i['full_name'].split()
    clear_dict['first_name']=name_split[0]
    clear_dict['last_name']=name_split[1]
    clear_dict['email']=i['email']
    clean_user.append(clear_dict)
for i in clean_user:
    print(i)    