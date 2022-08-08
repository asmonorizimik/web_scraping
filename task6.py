import json
with open('task_5.json','r') as file:
    details=json.load(file)
def language():
    d={}
    i=0
    while i<len(details):
        lang=details[i]['language']
        if lang in d:
            d[lang]+=1
        else:
            d[lang]=1
        i+=1
    print(d)
    with open("task_6.json",'w') as file1:
        json.dump(d,file1,indent=5)
language()


