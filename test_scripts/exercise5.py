def calculate_fine(books1):
    for i in books1:
        if i['days_late']==0:
            late = 0
            print(f"the fine for your book {i['title']} is {late}")
        elif 1<=i['days_late']<=5:
            late= i['days_late']*10
            print(f"the fine for your book {i['title']} is {late}") 
        else:
            late = 50
            print(f"the fine for your book {i['title']} is {late}")
            
books_returned = [
    {'title': 'Python Basics', 'days_late': 2},
    {'title': 'Harry Potter', 'days_late': 0},
    {'title': 'Algorithms', 'days_late': 7}
]
calculate_fine(books_returned)