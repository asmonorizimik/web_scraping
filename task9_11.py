import json
with open('task_5.json','r') as file:
    details=json.load(file)
def language():
    d={}
    i=0
    while i<len(details):
        genre=details[i]['genre']
        # print(genre)
        for j in genre:
            if j in d:
                d[j]+=1
            else:
                d[j]=1
        i+=1
    print(d)
    with open("task_9.json",'w') as file1:
        json.dump(d,file1,indent=5)
language()
