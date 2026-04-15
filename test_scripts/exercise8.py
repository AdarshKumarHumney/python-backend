comments = [
    {"user": "Bot123", "text": "Buy crypto now!", "spam": True},
    {"user": "Adarsh", "text": "Great video!", "spam": False},
    {"user": "Troll55", "text": "You suck.", "spam": True},
    {"user": "FanBoy", "text": "Loved the explanation.", "spam": False}
]
approved_comments=[]
for comment in comments:
    comment_dict={}
    if comment['spam']==False:
        comment_dict['user']=comment['user']
        comment_dict['text']=comment['text']
        approved_comments.append(comment_dict)
    else:
        comment_dict['user']=comment['user']
        comment_dict['text']="[Hidden]"    
        approved_comments.append(comment_dict)
for approve in approved_comments:
    print(f"{approve['user']} commented {approve['text']}")               