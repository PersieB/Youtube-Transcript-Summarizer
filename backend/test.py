dicts = [
    {
        'text': 'Hey there',
        'start': 7.58,
        'duration': 6.13
    },
    {
        'text': 'how are you',
        'start': 14.08,
        'duration': 7.58
    },
     
] 
str1 = ""
for i in dicts:
    str1 += " "+i['text']
print(str1)
